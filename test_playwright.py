import pytest
from playwright.sync_api import expect
from pages import page_playground, page_simple_form_demo, page_drag_drop_sliders, page_input_form_submit
from time import sleep


# def test_scenario_1(setup):    
#     page = setup
    
#     playground_page = page_playground.PlaygroundPage(page)
#     simple_form_demo_page = page_simple_form_demo.SimpleFormDemo(page)
    
#     page.goto("/selenium-playground")
        
#     playground_page.select_playground_menu("Simple Form Demo")    
#     expect(page).to_have_url("/selenium-playground/simple-form-demo")  
      
#     message = "Welcome to LambdaTest"       
#     simple_form_demo_page.enter_message(message)
    
#     simple_form_demo_page.click_check_value()
#     expect(simple_form_demo_page.text_message).to_have_text(message)
    

# def test_scenario_2(setup):    
#     page = setup
    
#     playground_page = page_playground.PlaygroundPage(page)
#     drag_drop_slider_page = page_drag_drop_sliders.DragDropSliders(page)
    
#     page.goto("/selenium-playground")    
#     playground_page.select_playground_menu("Drag & Drop Sliders")
    
#     drag_drop_slider_page.do_slider("15", "95")
    
#     sleep(2)

def test_scenario_3(setup):    
    
    DATA_FORM_SUBMIT = {
        "Name": "Wallace Petrucci Neves",
        "Email": "wallacepetrucci@gmail.com",
        "Password": "test123",
        "Company": "KaBuM!",
        "Website": "www.kabum.com.br",
        "country": "US",
        "City": "São Paulo",
        "Address 1": "Rua dos Buritis, 925",
        "Address 2": "Jd Oriental",
        "State": "SP",
        "Zip code": "04321002"
    }
    
    page = setup
    
    playground_page = page_playground.PlaygroundPage(page)
    input_form_submit_page = page_input_form_submit.InputFormSubmit(page)
    
    page.goto("/selenium-playground")    
    playground_page.select_playground_menu("Input Form Submit")
    
    input_form_submit_page.submit_form()
    
      
    input_form_submit_page.fill_all_fields(DATA_FORM_SUBMIT)