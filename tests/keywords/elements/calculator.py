from typing import Optional

import dogtail
from easyprocess import EasyProcess
from dogtail import tree


class Calculator:
    def __init__(self) -> None:
        self.process = EasyProcess(['gnome-calculator']).start()
        self.application = tree.root.application('gnome-calculator')

    def enter(self, expression: str) -> None:
        for char in expression.replace(' ', ''):
            self.click_widget(char)

    def calculate(self) -> None:
        self.click_widget('=')

    @property
    def running(self) -> bool:
        return self.process.is_alive()

    @property
    def result(self) -> Optional[str]:
        container = self.application.findChild(dogtail.predicate.GenericPredicate(roleName='viewport'))
        try:
            items = container.findChildren(dogtail.predicate.GenericPredicate(roleName='list item'))
            result_text = items[-1].child(roleName='label').text
        except tree.SearchError:
            result_text = None
        return result_text

    def close(self) -> None:
        self.process.stop()

    def click_widget(self, label) -> None:
        for widget in self.application.findChildren(dogtail.predicate.GenericPredicate(label)):
            if widget.visible and widget.position >= (0, 0):
                widget.click()
                break
