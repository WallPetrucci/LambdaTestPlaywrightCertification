class InputFormSubmit:
    
    def __init__(self, page) -> None:
        self.page = page
        self.input_company = self.page.locator("#company")
    
    def fill_all_fields(self, data):
        for field_name, value in data.items():
            
            if field_name == "country":
                self.select_option(value)
                continue
                
            self.page.get_by_placeholder(field_name).fill(value)
    
    def submit_form(self):
        self.page.get_by_role("button", name="Submit").click()
        
    def select_option(self, option):
        self.input_company.select_option(option)
    
    