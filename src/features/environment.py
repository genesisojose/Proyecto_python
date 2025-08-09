from selenium import webdriver
from src.page.Basepage import Basepage


def before_all(context):
    """Se ejecuta una vez, antes de TODOS los tests"""
    print(">>> Iniciando suite de pruebas")

def after_all(context):
    """Se ejecuta una vez, al final de TODOS los tests"""
    pass

def before_feature(context, feature):
    """Se ejecuta antes de cada Feature"""
    pass

def after_feature(context, feature):
    """Se ejecuta después de cada Feature"""
    pass

def before_scenario(context: object, scenario: object) -> None:
    """Se ejecuta antes de cada Scenario"""
    #print(f">>> Iniciando Scenario: {scenario.name}")
    base=Basepage()
    context.driver, context.wait = base.setup_driver()

def after_scenario(context, scenario):
    """Se ejecuta después de cada Scenario"""

    context.driver.quit()   # Cerrar navegador

def before_step(context, step):
    """Se ejecuta antes de cada Step"""
    pass

def after_step(context, step):
    """Se ejecuta después de cada Step"""
    #if step.status == "failed":
        #print(f"  !!! Falló el step: {step.name}")
    pass