
            ### ###           ###               ###    ### ###          #############          ##############   ###       ###        ###
            ### ###           ### ###           ###    ###    ###       ###       ###          ############     ###       ###        ###
         ###       ###        ###   ###         ###    ###       ###    ###         ###        ###              ###       ###        ###
         ###       ###        ###      ###      ###    ###        ###   ###         ###        ############     ###       ###        ###
       ### ######## ###       ###         ###   ###    ###        ###   ### #########          ############       ###     ###      ###
       ###           ###      ###           ### ###    ###       ###    ###         ###        ###                  ###   ###   ###
     ###               ###    ###            ## ###    ###    ###       ###           ###      ############           ### ### ###
     ###               ###    ###               ###    ### ###          ###             ###    ##############         ### ### ###

                                    ###                 ###           ### ###         ###                   ###
                                    ###                 ###           ### ###          ###                 ###
                                    ###                 ###        ###       ###         ###             ###
                                    ###                 ###        ###       ###         ###             ###
                                    ###                 ###      ### ######### ###          ###       ###
                                    ###                 ###      ###           ###          ###       ###
                                      ###################      ###               ###           ### ###
                                       #################       ###               ###           ### ###


import flet as ft
from VectorPointPlanner import VectorPointPlanner


async def main(page: ft.Page):
    vvp = VectorPointPlanner(page)
    vvp.setup()


ft.app(target=main)
#ft.app(main, view=ft.AppView.WEB_BROWSER)