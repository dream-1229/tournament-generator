from    openpyxl        import load_workbook
from    openpyxl.styles import Font
import  datetime

from    data       import cell_address



def create_excel_file(soccer_list,       soccer_num,
            basketball_list,    basketball_num,
            volleyball_list,    volleyball_num,
            dodgeball_list,     dodgeball_num):
    
    wb=load_workbook("tornament_standard.xlsx")

    ws_soccer       = wb[str(soccer_num)]
    for i in range(soccer_num):
        ws_soccer[cell_address[soccer_num][i]]          = soccer_list[i]
        cell        = ws_soccer[cell_address[soccer_num][i]]
        cell.font   = Font(size=20, bold=True)
    ws_soccer["F1"]     = "サッカー"
    ws_soccer.title     = "サッカー"

    ws_basketball   = wb[str(basketball_num)]
    for i in range(basketball_num):
        ws_basketball[cell_address[basketball_num][i]]  = basketball_list[i]
        cell        = ws_basketball[cell_address[basketball_num][i]]
        cell.font   = Font(size=20, bold=True)
    ws_basketball["F1"]   = "バスケ"
    ws_basketball.title   = "バスケ"

    ws_volleyball   = wb[str(volleyball_num)]
    for i in range(volleyball_num):
        ws_volleyball[cell_address[volleyball_num][i]]  = volleyball_list[i]
        cell        = ws_volleyball[cell_address[volleyball_num][i]]
        cell.font   = Font(size=20, bold=True)
    ws_volleyball["F1"]   = "バレー"
    ws_volleyball.title   = "バレー"

    ws_dodgeball    = wb[str(dodgeball_num)]
    for i in range(dodgeball_num):
        ws_dodgeball[cell_address[dodgeball_num][i]]    = dodgeball_list[i]
        cell        = ws_dodgeball[cell_address[dodgeball_num][i]]
        cell.font   = Font(size=20, bold=True)
    ws_dodgeball["F1"]    = "ドッヂ"
    ws_dodgeball.title    = "ドッヂ"

    
    used_sheet   = [str(soccer_num), str(basketball_num), str(volleyball_num), str(dodgeball_num), "timetable"]
    delete_sheet  = [c for c in wb.sheetnames if c not in used_sheet]
    for sheet in delete_sheet:
        del wb[sheet]

    
    now         = datetime.datetime.now()
    filename    = f"{now.year-2000}{now.month:02d}{now.day:02d}.xlsx"
    wb.save(filename)
