from ipywidgets import interactive
import ipywidgets as widgets

import matplotlib.pyplot as plt
import numpy as np
import math

from matplotlib.ticker import FuncFormatter as ff


driving_color = "#1f78b4"
delivering_color = "#b2df8a"
rungis_color = "#a6cee3"

time = {'4:00': 240,
        '4:15': 255,
        '4:30': 270,
        '4:45': 285,
        '5:00': 300,
        '5:15': 315,  
        '5:30': 330,
        '5:45': 345,
        '6:00': 360,
        '6:15': 375,
        '6:30': 390,
        '6:45': 405,
        '7:00': 420, 
        '7:15': 435, 
        '7:30': 450,
        '7:45': 465,
        '8:00': 480,
        '8:15': 495,
        '8:30': 510,
        '8:45': 525,
        '9:00': 540, 
        '9:15': 555, 
        '9:30': 570,
        '9:45': 585,
        '10:00': 600,
        '10:15': 615,
        '10:30': 630,
        '10:45': 645,
        '11:00': 660, 
        '11:15': 675, 
        '11:30': 690,
        '11:45': 705,
        '12:00': 720,
        '12:15': 735,
        '12:30': 750,
        '12:45': 765,
        '13:00': 780, 
        '13:15': 795, 
        '13:30': 810,
        '13:45': 825,
        '14:00': 840,
        '14:15': 855,
        '14:30': 870,
        '14:45': 885,
        '15:00': 900, 
        '15:15': 915, 
        '15:30': 930,
        '15:45': 945,
        '16:00': 960,
        '16:15': 975,
        '16:30': 990,
        '16:45': 1005,
        '17:00': 1020, 
        '17:15': 1035, 
        '17:30': 1050,
        '17:45': 1065,
        '18:00': 1080,
        '18:15': 1095,
        '18:30': 1110,
        '18:45': 1125,
        '19:00': 1140, 
        '19:15': 1155, 
        '19:30': 1170,
        '19:45': 1185,
        '20:00': 1200, 
        '20:15': 1215, 
        '20:30': 1230,
        '20:45': 1245,
        '21:00': 1260,
        '21:15': 1275,
        }

orders = {
          '5 orders': 0,
          '10 orders': 1,
          '15 orders': 2, 
          '20 orders': 3,
          '25 orders': 4,
          '30 orders': 5,
          '35 orders': 6,
          '40 orders': 7,
          '45 orders': 8,
          '50 orders': 9,
         }

nb_clients = {'5 clients': 0,
           '6 clients': 1,
           '7 clients': 2,
           '8 clients': 3,
           '9 clients': 4,
           '10 clients': 5,
           '11 clients': 6,
           '12 clients': 7,
           '13 clients': 8,
           '14 clients': 9,
           '15 clients': 10,
           '16 clients': 11,
           '17 clients': 12,
           '18 clients': 13,
           '19 clients': 14,
           '20 clients': 15,
           '25 clients': 16,
           '30 clients': 17,
           '35 clients': 18,
           '40 clients': 19,
           '45 clients': 20,
           '50 clients': 21}


hot_fix_clients = [5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15,
           16, 17, 18, 19, 20, 25, 30, 35, 40, 45, 50]

dropoff_time = {'1 min': 1,
                '2 min': 2, 
                '3 min': 3,
                '4 min': 4,
                '5 min': 5,
                '7 min': 7,
                '8 min': 8,
                '9 min': 9,
                '10 min': 10,
                '11 min': 11,
                '12 min': 12,
                '13 min': 13,
                '14 min': 14,
                '15 min': 15,
                '20 min': 20,
                '25 min': 25,
                '30 min': 30,
                '35 min': 35,
                '40 min': 40}


# axis 1 : capacity 5, 10, 15, 20, 25, 30, 35, 40, 45,50
# axis 0 : nb clients 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19,
# 20, 25, 30, 35, 40, 45, 50

time_sim_results = [
[9.5, 9.5, 9.5, 9.5, 9.5, 9.5, 9.5, 9.5, 9.5, 9.5],
[2.3, 9.1, 9.1, 9.1, 9.1, 9.1, 9.1, 9.1, 9.1, 9.1],
[2.6, 8.1, 8.1, 8.1, 8.1, 8.1, 8.1, 8.1, 8.1, 8.1],
[3.3, 7.2, 7.2, 7.2, 7.2, 7.2, 7.2, 7.2, 7.2, 7.2],
[3.2, 6.8, 6.8, 6.8, 6.8, 6.8, 6.8, 6.8, 6.8, 6.8],
[3 ,  6.6, 6.6, 6.6, 6.6, 6.6, 6.6, 6.6, 6.6, 6.6],
[1.8, 3,   6.4, 6.4, 6.4, 6.4, 6.4, 6.4, 6.4, 6.4],
[1.8, 2.8, 6.2, 6.2, 6.2, 6.2, 6.2, 6.2, 6.2, 6.2],
[1.7, 2.7, 6,   6,   6,   6,   6,   6,   6,   6],
[1.7, 2.7, 5.9, 5.9, 5.9, 5.9, 5.9, 5.9, 5.9, 5.9],
[1.7, 2.6, 5.7, 5.7, 5.7, 5.7, 5.7, 5.7, 5.7, 5.7],
[1.1, 2.5, 2.5, 5.6, 5.6, 5.6, 5.6, 5.6, 5.6, 5.6],
[1.1, 2.5, 2.5, 5.5, 5.5, 5.5, 5.5, 5.5, 5.5, 5.5],
[1.1, 2.5, 2.5, 5.3, 5.3, 5.3, 5.3, 5.3, 5.3, 5.3],
[1,   2.5, 2.5, 5.3, 5.3, 5.3, 5.3, 5.3, 5.3, 5.3],
[0.9, 2.4, 2.4, 5,   5,   5,   5,   5,   5, 5],
[0.9, 1.4, 2.4, 2.4, 4.5, 4.6, 4.6, 4.6, 4.6, 4.6],
[0.6, 1.3, 2.4, 2.5, 2.2, 4.4, 4.4, 4.4, 4.4, 4.4],
[0.4, 1.3, 1.4, 2.5, 2.2, 2.3, 4.4, 4.4, 4.4, 4.4],
[0.3, 1.1, 1.3, 2.5, 2.2, 2.2, 2.3, 4.3, 4.3, 4.4],
[0.3, 1,   1.2, 1.3, 2.2, 2.3, 2.3, 2.3, 4.2, 4.4],
[0.3, 0.6, 1,   1.3, 2.2, 2.4, 2.4, 2.2, 2.2, 4.4]]

vehicle_sim_results = [
[1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
[2, 1, 1, 1, 1, 1, 1, 1, 1, 1],
[2, 1, 1, 1, 1, 1, 1, 1, 1, 1],
[2, 1, 1, 1, 1, 1, 1, 1, 1, 1],
[2, 1, 1, 1, 1, 1, 1, 1, 1, 1],
[2, 1, 1, 1, 1, 1, 1, 1, 1, 1],
[3, 2, 1, 1, 1, 1, 1, 1, 1, 1],
[3, 2, 1, 1, 1, 1, 1, 1, 1, 1],
[3, 2, 1, 1, 1, 1, 1, 1, 1, 1],
[3, 2, 1, 1, 1, 1, 1, 1, 1, 1],
[3, 2, 1, 1, 1, 1, 1, 1, 1, 1],
[4, 2, 2, 1, 1, 1, 1, 1, 1, 1],
[4, 2, 2, 1, 1, 1, 1, 1, 1, 1],
[4, 2, 2, 1, 1, 1, 1, 1, 1, 1],
[4, 2, 2, 1, 1, 1, 1, 1, 1, 1],
[4, 2, 2, 1, 1, 1, 1, 1, 1, 1],
[5, 3, 2, 2, 1, 1, 1, 1, 1, 1],
[6, 3, 2, 2, 2, 1, 1, 1, 1, 1],
[8, 4, 3, 2, 2, 2, 1, 1, 1, 1],
[8, 4, 3, 2, 2, 2, 2, 1, 1, 1],
[10,5, 3, 3, 2, 2, 2, 2, 1, 1],
[11,6, 4, 3, 2, 2, 2, 2, 2, 1]]

def m2hm(x, i):
    h = int(x/60)
    m = int(x%60)
    return '%(h)02d:%(m)02d' % {'h':h,'m':m}
 

def f(clients, capacity, dropoff, dw, dw_start, dw_end, tw, tw_start, tw_end, far_dc):
    

    #first_leg_time = math.ceil(b.avg_first_leg*60/50000)
    first_leg_time = 700*60/20000


    #tour_time = math.ceil(b.avg_tour*60/20000)*6
    tour_time = time_sim_results[clients][capacity]*(hot_fix_clients[clients]/vehicle_sim_results[clients][capacity])

    time_dropoff = dropoff*hot_fix_clients[clients]/vehicle_sim_results[clients][capacity]

    #return_leg_time = math.ceil(b.avg_return_leg*60/50000)
    return_leg_time = 2500*60/20000
    
    time_rungis = 15000*60/35000

    print('The fleet is composed of ' + str(vehicle_sim_results[clients][capacity]) + " vehicles.")
    print('The average driving time between two deliveries is ' + str(time_sim_results[clients][capacity]) + " min.")
    print('Each vehicle delivers in average ' + str(round(hot_fix_clients[clients]/vehicle_sim_results[clients][capacity])) + " clients.")

    print("Therefore, average total driving time is " + str(tour_time) + " min." )


    city_line_width = 3
    line_width = 3
    
    if far_dc:
        
        fig2, ax2 = plt.subplots()
        
        """ax2.bar(0, 30, bottom=b.avg_first_leg, color = r_color)
        ax2.bar(1, 0, bottom=b.avg_tour, color = r_color)
        ax2.bar(2, 30, bottom=b.avg_return_leg+b.avg_first_leg + b.avg_tour, color = r_color)"""
        
        ax2.bar(0, first_leg_time, bottom = dw_start, color = driving_color)
        ax2.bar(0, time_rungis, bottom= dw_start + first_leg_time, color = rungis_color, label="Rungis")
        
        ax2.axhline(y=dw_start + first_leg_time + time_rungis, linewidth=city_line_width, 
                    color='#CDC7C6', linestyle='-', label="In city", zorder=2)
        
        ax2.bar(1, tour_time, bottom = dw_start + first_leg_time + time_rungis, color = driving_color, label="Driving")
        ax2.bar(1, time_dropoff, bottom=dw_start + first_leg_time + time_rungis + tour_time, color = delivering_color, label="Delivering       ")
        
        ax2.axhline(y=dw_start + first_leg_time + time_rungis + tour_time + time_dropoff, color='#CDC7C6', linestyle='-', linewidth=city_line_width, zorder=2)
        
        ax2.bar(2, return_leg_time, bottom=dw_start + first_leg_time + time_rungis + tour_time + time_dropoff, color = driving_color)
        ax2.bar(2, time_rungis, bottom= dw_start + first_leg_time + time_rungis + tour_time + time_dropoff + return_leg_time, color = rungis_color)
        
        ax2.set_ylim(dw_start-100, dw_start + first_leg_time + time_rungis + tour_time + time_dropoff + return_leg_time + time_rungis + 100)
        
    else:
        fig2, ax2 = plt.subplots()
        ax2.bar(0, first_leg_time, bottom=dw_start, color = driving_color)
        
        ax2.axhline(y=dw_start + first_leg_time, color='#CDC7C6', linestyle='-', linewidth=city_line_width, zorder=2)
        
        ax2.bar(1, tour_time, bottom=first_leg_time+dw_start, color = driving_color, label="Driving")
        ax2.bar(1, time_dropoff, bottom=first_leg_time+tour_time+dw_start, color = delivering_color, label="Delivering       ")
        
        ax2.axhline(y=dw_start + first_leg_time + tour_time + time_dropoff, color='#CDC7C6', linestyle='-', label="Within city", linewidth=city_line_width, zorder=2)

        ax2.bar(2, return_leg_time, bottom=first_leg_time + tour_time+dw_start+time_dropoff, color = driving_color)
        
        ax2.set_ylim(dw_start-100, dw_start + first_leg_time + time_rungis + tour_time + time_dropoff + return_leg_time + time_rungis + 100)

    ax2.yaxis.set_major_formatter(ff(m2hm))

    # Working day
    dw_color = "#008240"
    if dw:
        ax2.axhline(y=dw_start, color=dw_color, linestyle='-', label="Time shift", linewidth=line_width, zorder=2)
        ax2.axhline(y=dw_end, color=dw_color, linestyle='-', linewidth=line_width, zorder=2)
    
    # Time window from clients or city
    tw_color = "#A0211B"

    if tw:
        ax2.axhline(y=tw_start, color=tw_color, linestyle='--', label="Time Window", linewidth=line_width, zorder=2)
        ax2.axhline(y=tw_end, color=tw_color, linestyle='--', linewidth=line_width, zorder=2)
    
    
    ax2.set_title("Average working shift of the fleet – #" + str(vehicle_sim_results[clients][capacity]) + " vehicle(s)")
    ax2.set_xticklabels(["", "", "First leg", "", "Tour", "", "Return leg"])
    ax2.tick_params(bottom=False)
    ax2.legend(bbox_to_anchor=(1.05, 1), loc=2)
    
    fig2.set_size_inches(15.5, 9.5)



    

interactive_plot = interactive(f,
                               dw=widgets.Checkbox(
                                            value=False,
                                            description='Show workers shift on the road',
                                            disabled=False),
                               dw_start = widgets.Dropdown(
                                        options=time,
                                        value=510,
                                        description='starts at:'),
                               dw_end = widgets.Dropdown(
                                        options=time,
                                        value=780,
                                        description='ends at:'),
                               tw=widgets.Checkbox(
                                            value=False,
                                            description='Show time window',
                                            disabled=False),
                               tw_start = widgets.Dropdown(
                                        options=time,
                                        value=540,
                                        description='starts at:'),
                               tw_end = widgets.Dropdown(
                                        options=time,
                                        value=690,
                                        description='ends at:'),
                               clients= widgets.Dropdown(
                                        options=nb_clients,
                                        value=21,
                                        description='Nb clients:'),                             
                               capacity = widgets.Dropdown(
                                        options=orders,
                                        value=2,
                                        description='Vehicle capacity:'),
                               dropoff = widgets.Dropdown(
                                        options=dropoff_time,
                                        value=11,
                                        description='Dropoff duration:'),
                               far_dc=widgets.Checkbox(
                                            value=True,
                                            description='Distribution Center in Rungis',
                                            disabled=False)


                               )




interactive_plot


## add config for the La poste and Pomona
## add legend