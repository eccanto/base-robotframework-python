from robot.api.deco import keyword


@keyword('open calculator')
def open_calculator():
    pass


@keyword('close calculator')
def close_calculator():
    pass


@keyword('the calculator is open')
def is_open():
    pass


@keyword('the expression "5 + 5" is entered')
def enter_expression():
    pass


@keyword('I press the calculate button')
def calculate():
    pass


@keyword('the result shown is "10"')
def check_result():
    pass
