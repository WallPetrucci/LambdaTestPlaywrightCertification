class DragDropSliders:
    def __init__(self, page) -> None:
        self.page = page
        self.slider = "input[value='{}']"
        self.range_success =  self.page.locator("#rangeSuccess")
        
    def do_slider(self, slider_number_start, slider_number_end):
        slider = self.page.locator(self.slider.format(slider_number_start))
        slider_box = slider.bounding_box()
        print(slider.bounding_box())
        
        self.page.locator(self.slider.format(slider_number_start)).hover(position={ "x": 0, "y": 0 })
        self.page.mouse.down()
        self.page.locator(self.slider.format(slider_number_start)).hover(position={ "x": slider_box['width'], "y": 0 })
        self.page.mouse.up()