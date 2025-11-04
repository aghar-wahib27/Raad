from .ui import * 


def create(**kargs):
    new_ui=ui(_name=kargs['name'])
    for comp in new_ui.de.data['components']:
        c=SYSTEMS['ui'].general_components[comp['type']](_name=comp['name'],parent=new_ui)
        new_ui.components.append(c)

    all_nodes=NodeFlatten(new_ui.children)
    new_ui.all_nodes=all_nodes
    sizing_groups={k:[] for k in ['fixed','fit_w','grow',"per_w",'fit_h',"per_h"]}
    for node in [i for i in all_nodes if i.t!='leaf']:
            sizing_groups[node.size_data['w'][0]].append(node)
            sizing_groups[node.size_data['h'][0]].append(node)

    

    for nodes in list(sizing_groups.values())[:4]:
        for node in nodes:
            node.resize()

    WrapText(all_nodes)

    for nodes in list(sizing_groups.values())[2:]:
        for node in nodes:
            node.resize()

    new_ui.NodePositioning()


    return new_ui


