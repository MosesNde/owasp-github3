 	QWidget,
 )
 
 from .paramters_tab import ParamtersTab
 from .search_tab import SearchTab
 
 		tabs.setTabPosition(QTabWidget.TabPosition.West)
 		tabs.setMovable(True)
 
 		self.search_tab = SearchTab()
 		self.paramters_tab = ParamtersTab()
 
 		tabs.addTab(self.search_tab, "Search")
 		tabs.addTab(self.paramters_tab, "Parameters")
 
 		page_layout = QVBoxLayout()