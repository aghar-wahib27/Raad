__doc__ = """
* This creation mehtods can only be used for platformers ,
* To use them apropretly your csv should follow two rules :
    1- ALWAYS leave the last column empty
    2- while using getGroupedRectList never start two blocks and end them at the same column or they would be considered one block and the second one will vanish
* Of course I inetend to fix those two problems at future realeses 
"""

from .allModules import pygame

def getRectListFromCsv(csv_file_content:list[list],rect_put_value:int=1,size=[20,20]):
    rect_list = []
    for row_index,row in enumerate( csv_file_content ) :
        for col_index,col in enumerate(row) :
            if int(col) == rect_put_value :
                rect_list.append(pygame.Rect(col_index*size[0],row_index*size[1],20,20))

    return rect_list

def getGroupedRectListUponWidth(csv_file_content:list[list],rect_put_value:int=1,empty_value:int=-1,size=[20,20]):
    rect_list = []
    for row_index,row in enumerate( csv_file_content ) :
        new_rect_info = { 'start':[ 0,0 ] , 'ctr':0 }
        for col_index,col in enumerate(row) :
            if int(col) == rect_put_value :
                if new_rect_info['ctr'] == 0:
                    new_rect_info[ 'start' ] = [col_index,row_index]
                new_rect_info[ 'ctr' ] += 1
            if ( int(col) == empty_value and new_rect_info['ctr'] )or col_index == len(row) :
                print(new_rect_info)
                rect_list.append(
                        pygame.Rect(
                            new_rect_info['start'][0] * size[0],
                            new_rect_info['start'][1] * size[1],
                            size[0] * new_rect_info['ctr'],
                            size[1]
                            )
                        )
                new_rect_info = { 'start':[ 0,0 ] , 'ctr':0 }
    return rect_list

def getGroupedRectList(csv_file_content:list[list],rect_put_value:int=1,empty_value:int=-1,size=[20,20]):
    rect_dict = {}
    for row_index,row in enumerate( csv_file_content ) :
        new_rect_info = { 'start':[ 0,0 ] , 'ctr':0 }
        for col_index,col in enumerate(row) :
            if int(col) == rect_put_value :
                if new_rect_info['ctr'] == 0:
                    new_rect_info[ 'start' ] = [col_index,row_index]
                new_rect_info[ 'ctr' ] += 1
            if ( int(col) == empty_value and new_rect_info['ctr'] )or col_index == len(row) :

                # print(new_rect_info)
                if f"{new_rect_info['start'][0]}+{new_rect_info['ctr']}" in rect_dict:
                    rect_dict[f"{new_rect_info['start'][0]}+{new_rect_info['ctr']}"]['height'] += 1
                else : 
                    rect_dict[f"{new_rect_info['start'][0]}+{new_rect_info['ctr']}"]= {'start':new_rect_info['start'],"width":new_rect_info['ctr'],"height" : 1}
 
                new_rect_info = { 'start':[ 0,0 ] , 'ctr':0 }
    rect_list = [
                    pygame.Rect(
                        info['start'][0] * size[0],
                        info['start'][1] * size[1],
                        info['width'] * size[0],
                        info['height'] * size[1]
                        )
                    for info in rect_dict.values()
                 ]
    return rect_list


