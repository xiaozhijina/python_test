# coding:utf8

#import  pygal
import  pygal.maps.world

wm = pygal.maps.world.World()
wm.title  = "North ,central ,and south America"
wm.add('North American',{'ca':150000,'mx':120000,'us':12})
wm.add('Central American',{
    'bz':212121,'cr':212121212,'gt':5555555,
    'hn':2332323,'ni':3232424424,'pa':12121212,'sv':123333})
wm.render_to_file('americas.svg')
#for cuntry_code in sorted(COUNTRIES.keys()):
#    print(cuntry_code,COUNTRIES[cuntry_code])
worldmap_chart = pygal.maps.world.World()
worldmap_chart.title = 'Some countries'
worldmap_chart.add('F countries', ['fr', 'fi'])
worldmap_chart.add('M countries', ['ma', 'mc', 'md', 'me', 'mg',
                                   'mk', 'ml', 'mm', 'mn', 'mo',
                                   'mr', 'mt', 'mu', 'mv', 'mw',
                                   'mx', 'my', 'mz'])
worldmap_chart.add('U countries', ['ua', 'ug', 'us', 'uy', 'uz'])
worldmap_chart.render_to_file('some.svg')
