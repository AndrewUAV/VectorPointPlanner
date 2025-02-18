''' The main window of GUI '''
import flet as ft

from Map import Map
from styles.Page import Page
from styles.Button import Button


class VectorPointPlanner:
    def __init__(self):
        self.vector_point_planner_page = Page(_title='VectorPointPlanner')
        self.map = Map()

        """ CREATE BUTTON """
        self.button_data_creator = Button(text='Data', on_click='data_click')
        self.button_plan_creator = Button(text='Plan mission', width=150, on_click='mission_planning_click')
        self.button_settings_creator = Button(text='Settings', width=150, on_click='settings_click')


        """ GET BUTTON """
        self.button_data = self.button_data_creator.create_button()
        self.button_plan = self.button_plan_creator.create_button()
        self.button_settings = self.button_settings_creator.create_button()


    def add_buttons_like_row(self, list_buttons):
        return ft.Row(controls=list_buttons)


    def get_page(self, page: ft.Page):
        self.vector_point_planner_page.setup_page(page)

        """ ADD BUTTONS """
        main_buttons_row = self.vector_point_planner_page.add_buttons_like_row(list_buttons=[self.button_data,
                                                                                             self.button_plan,
                                                                                             self.button_settings])
        page.add(main_buttons_row)

        """ ADD MAP """
        page.add(self.map.create_map())

