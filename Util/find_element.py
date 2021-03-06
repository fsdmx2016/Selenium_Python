# coding=utf-8
from Util.read_init import ReadIni


class findElement:
    def __init__(self, driver):
        self.driver = driver

    def get_element(self, key):
        read_ini = ReadIni()
        local = read_ini.get_value(key)
        if local != None:
            by = local.split('>')[0]
            local_by = local.split('>')[1]
            try:
                if by == 'id':
                    return self.driver.find_element_by_id(local_by)
                elif by == 'className':
                    return self.driver.find_element_by_class_name(local_by)
                elif by == 'classNames':
                    return self.driver.find_elements_by_class_name(local_by)
                elif by == 'name':
                    return self.driver.find_element_by_name(local_by)
                elif by == 'link_text':
                    return self.driver.find_element_by_link_text(local_by)
                elif by == 'compose':
                    return self.driver.find_element_by_class_name("form-vertical").find_elements_by_class_name("form-group")[3]
                else:
                    return self.driver.find_element_by_xpath(local_by)
            except:
                # self.driver.save_screenshot("../jpg/test02.png")
                return None
        else:
            return None
