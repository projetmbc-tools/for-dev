#! /usr/bin/env python3

###
# This module ???
###

from os import getcwd, popen
from subprocess import run

from spkpb import *

from .lowlevel import *


# ----------------------- #
# -- PROJECT MANAGMENT -- #
# ----------------------- #

###
# This class ????
###

class Project(LowLevel):
###
# prototype::
#     :see: = lowlevel.LowLevel
###
    def __init__(
        self,
        project: Union[str, Path],
        source : Union[str, Path],
        target : Union[str, Path],
        ignore : str  = '',
        usegit : bool = False,
    ):
        super().__init__(
            project = project,
            source  = source,
            target  = target,
            ignore  = ignore,
            usegit  = usegit,
        )


###
# This method builds the list of file to copy from source to target.
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
# This method ...
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
# This method ...
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
        self._indicating_lof_found(
            whatused = 'the value of "ignore"'
        )


###
# This method ...
#
# info::
#     Because the method ``rungit`` fails with ``options = ['check-ignore', '**/*'])``, 
#     we must test directly each path.
###
    def removed_by_git(self) -> None:
        len_lof_before = len(self.lof)

# Let's talk.
        self.recipe(
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
            whatused = '"git"',
            extra    = extra
        )


###
# This method ...
###
    def _indicating_lof_found(
        self,
        whatused: str,
        extra   : str = ''
    ) -> None: 
        len_lof = len(self.lof)
        plurial = '' if len_lof == 1 else 's'

        self.recipe(
            {VAR_STEP_INFO: 
                f'{len_lof} file{plurial} found using {whatused}.{extra}'},
        )