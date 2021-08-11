#! /usr/bin/env python3

###
# This module implements all the logic needed to manage one project.
###

from spkpb import *

from .lowlevel import *


# ------------------------ #
# -- PROJECT MANAGEMENT -- #
# ------------------------ #

###
# This class is the main one to use such as to easily to manage a project using 
# the "source-to-final-product" workflow.
###

class Project(LowLevel):
###
# prototype::
#     opensession  = ; // See Python typing...
#                    ``True`` is to open the communication and 
#                    ``False`` starts directly the work.
#     closesession = ; // See Python typing...
#                    ``True`` is to close the communication and 
#                    ``False`` is to no do it.
#              
#
# This method is the great bandleader building the list of files to be copied to
# the target final dir.
###
    def build(
        self,
        opensession : bool = True,
        closesession: bool = True,
    ) -> None:
# List of methods called.
        methodenames = ['reset']

        if opensession:
            methodenames.append('open_session')

        if self.usegit:
            methodenames.append('check_git')

        methodenames += [
            'files_without_git',
        ]

        if self.usegit:
            methodenames.append('removed_by_git')

# Let's work.
        for name in methodenames:
            getattr(self, name)()

            if not self.success:
                break

# We always close the session.
        if closesession:
            self.close_session()

###
# This method does three things.
#
#     1) Indirecty it checks that ¨git can be used.   
#     2) It finds the branch on which we are working.
#     3) It verifies that there isn't any uncommitted changes in the source files.
#
# warning::
#     We do not want any uncommitted changes even on the ignored files because this
#     could imply some changes in the final product. 
###
    def check_git(self) -> None:
        self.recipe(
            {VAR_STEP_INFO: f'Checking "git".'}
        )

# Let's go
        infos = {}

        for kind, options in [
# Current branch.
            ('branch', ['branch']),
# We don't want uncommitted files in our source folder!
            ('uncommitted', ['a']),
        ]:
            infos[kind] = self.rungit(options)
    
            if not self.success:
                return

# Branch used.
        for onebranch in infos['branch'].split('\n'):
            if onebranch.startswith('*'):
                branch = onebranch[1:].strip()
                break

        self.recipe(
            {VAR_STEP_INFO: f'Working in the branch "{branch}".'}
        )

# Uncommitted changes in our source?
        tosearch = f'{self.project}/{self.source.name}/'

        if (
            "Changes to be committed" in infos['uncommitted']
            and
            tosearch in infos['uncommitted']
        ):
            gitinfos = [
                x.strip()
                for x in infos['uncommitted'].split('\n')
                if tosearch in x
            ]

            nb_changes = len(gitinfos)
            howmany    = 'one' if nb_changes == 1 else 'several'
            plurial    = ''    if nb_changes == 1 else 's'

            fictive_tab = '\n    + '
            gitinfos    = fictive_tab.join(gitinfos)

            self.new_error(
                what = self.source,
                info = (
                    f'{howmany} uncommitted file{plurial} found in the source folder. '
                     'See below.'
                    f'{fictive_tab}{gitinfos}'
                ),
                level = 1
            )
            return


###
# This method builds the list of files to keep just by using the ignore rules.
#
# info::
#     ¨git is not used here.
###
    def files_without_git(self) -> None:
# Let's talk.
        self.recipe(
            {VAR_STEP_INFO: 
                 'Start the analysis of the source folder:'
                 '\n'
                f'"{self.source}".'},
        )

# Does the source dir exist?
        if not self.source.is_dir():
            self.new_error(
                what = self.source,
                info = (
                     'source folder not found:'
                     '\n'
                    f'"{self.source}"'
                ),
            )
            return

# List all the files.
        self.lof = [
            f for f in self.iterfiles(self.source)
        ]

# An empty list stops the process.
        if not self.lof:
            self.new_critical(
                what = self.source,
                info = 'empty source folder.',
            )
            return

# Let's be proud of our 1st list.
        if self.usegit:
            whatused = 'the value of "ignore"'
        
        else:
            whatused = 'only the value of "ignore"'

            self._indicating_lof_found(
                output   = FORLOG,
                whatused = whatused
            )

        self._indicating_lof_found(
            output   = FORTERM,
            whatused = whatused
        )


###
# This method shrinks the list of files by using the ignore rules knwon by ¨git.
#
# info::
#     The method ``rungit`` fails with ``options = ['check-ignore', '**/*'])``, 
#     so we must test directly each path.
###
    def removed_by_git(self) -> None:
        len_lof_before = len(self.lof)

# Let's talk.
        self.recipe(
            FORTERM,
                {VAR_STEP_INFO: 
                    'Removing unwanted files using "git".'},
        )

        self.lof = [
            onefile
            for onefile in self.lof
            if not self.rungit(
                options = [
                    'check-ignore',
                    onefile.relative_to(self.project)
                ]
            )
        ]
        
# Let's be proud of our 2nd list.
        len_lof = len(self.lof)
        
        if len_lof_before == len_lof:
            extra = ' No new file ignored.'

        else:
            nb_new_ignored = len_lof_before - len_lof
            plurial        = '' if nb_new_ignored == 1 else 's'

            extra = (
                f' {nb_new_ignored} new file{plurial} '
                 'ignored thanks to "git".'
            )

        self._indicating_lof_found(
            output   = FORTERM,
            whatused = '"git"',
            extra    = extra
        )

        self._indicating_lof_found(
            output   = FORLOG,
            whatused = '"git" and the value of "ignore"',
        )


###
# prototype::
#     output   = _ in [FORTERM, FORLOG, FORALL]; // See Python typing...
#                the output(s) where we want to communicate.
#     whatused = ; // See Python typing...
#                the method used to shrink the list of files.
#     extra    = ( '' ); // See Python typing...
#                a small extra text.
#
# This method is just a factorization.
###
    def _indicating_lof_found(
        self,
        output  : str,
        whatused: str,
        extra   : str = ''
    ) -> None: 
        len_lof = len(self.lof)
        plurial = '' if len_lof == 1 else 's'

        self.recipe(
            output,
                {VAR_STEP_INFO: 
                    f'{len_lof} file{plurial} found using {whatused}.{extra}'},
        )