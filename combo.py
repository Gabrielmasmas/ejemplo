from PyQt5.QtCore import QEvent, QStringListModel
from PyQt5.QtGui import QPalette, QFontMetrics, QStandardItem, QStandardItemModel
from PyQt5.QtWidgets import QApplication, QMainWindow, QComboBox, QStyledItemDelegate, QListView, QAbstractItemView, \
    QCompleter, QLineEdit
from PyQt5.QtCore import Qt


class CheckableComboBox(QComboBox):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.setEditable(True)
        self.setInsertPolicy(QComboBox.NoInsert)

        # Make Completer for Search Box
        self.completer = QCompleter()
        self.completer.setFilterMode(Qt.MatchContains)
        self.completer.setCaseSensitivity(Qt.CaseInsensitive)

        # Make Search Box for Combo Box
        self.search_box = QLineEdit()
        self.search_box.setCompleter(self.completer)
        self.search_box.setFocus()
        self.search_box.selectAll()

        self.setLineEdit(self.search_box)
        self.completer.setModel(self.model())

    def addItem(self, text, data=None):
        item = QStandardItem()
        item.setText(text)
        if data is None:
            item.setData(text)
        else:
            item.setData(data)
        item.setFlags(Qt.ItemIsEnabled | Qt.ItemIsUserCheckable)
        item.setData(Qt.Unchecked, Qt.CheckStateRole)
        self.model().appendRow(item)

    def addItems(self, texts, datalist=None):
        for i, text in enumerate(texts):
            try:
                data = datalist[i]
            except (TypeError, IndexError):
                data = None
            self.addItem(text, data)



if __name__ == '__main__':
    app = QApplication([])
    region = ['South', 'North', 'East', 'West']
    combo = CheckableComboBox()
    combo.addItems(region)
    combo.show()
    app.exec()

