# SPDX-License-Identifier: CC0-1.0

from krita import Extension
from builtins import i18n
from . import uidocumenttools


class DocumentToolsExtension(Extension):

    def __init__(self, parent):
        super(DocumentToolsExtension, self).__init__(parent)

    def setup(self):
        pass

    def createActions(self, window):
        action = window.createAction("document_tools", i18n("Document Tools"))
        action.setToolTip(
            i18n("Plugin to manipulate properties of selected documents."))
        action.triggered.connect(self.initialize)

    def initialize(self):
        self.uidocumenttools = uidocumenttools.UIDocumentTools()
        self.uidocumenttools.initialize()
