import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import plotly.plotly as py 
from plotly.graph_objs import Scatter,Data

#from mpl_toolkits.basemap import Basemap
#from geopy.geocoders import Nominatim

df=pd.read_csv('cancer2017.csv',encoding='utf-8')
df.replace({r'[^\x00-\x7F]+':np.nan}, regex=True, inplace=True)
for i in range(0,df.shape[0]):
    for j in range(1,df.shape[1]):
        if ',' in str(df.iloc[i][j]):
            df.iloc[i][j]=df.iloc[i][j].replace(',','')
        df.iloc[i][j]=pd.to_numeric(df.iloc[i][j])
df.columns = [c.strip() for c in df.columns.values.tolist()]
df.columns = [c.replace(' ','') for c in df.columns.values.tolist()]

x='State'
y=list(df.columns)
i=1
z=["prostate","brain","breast","colon","leukemia","liver","lung","lymphoma","ovary","pancreas"]

fig,ax=plt.subplots(nrows=5,ncols=2,figsize=(20,20))
fig.suptitle('Incomplete Data Set')

for row in ax:
    for col in row:
        col.plot(df[x],df[y[i]])
        i=i+1
i=0
for ax in fig.axes:
    plt.xlabel('States')
    plt.ylabel("no of people affected")
    plt.title(z[i])
    i=i+1
    plt.sca(ax)
    plt.xticks(rotation=90)
    plt.grid()
    plt.subplots_adjust(left=None, bottom=None, right=None, top=None, wspace=None, hspace=1)

fig.tight_layout()
fig.subplots_adjust(top=0.95)
plt.savefig('line_incomplete.png',bbox_inches='tight')

bdf=df.copy()


#hide this line for incomplete data
for col in range(1,len(y)):
    bdf[y[col]].fillna((bdf[y[col]].mean()), inplace=True)

i=1
fig,ax=plt.subplots(nrows=5,ncols=2,figsize=(20,20))
fig.suptitle('NaN Filled Data Set')

for row in ax:
    for col in row:
        col.plot(bdf[x],bdf[y[i]])
        i=i+1
i=0
for ax in fig.axes:
    plt.xlabel('States')
    plt.ylabel("no of people affected")
    plt.title(z[i])
    i=i+1
    plt.sca(ax)
    plt.xticks(rotation=90)
    plt.grid()
    plt.subplots_adjust(left=None, bottom=None, right=None, top=None, wspace=None, hspace=1)

fig.tight_layout()
fig.subplots_adjust(top=0.95)
plt.savefig('line_complete.png',bbox_inches='tight')


#bar variant

i=1
fig,ax=plt.subplots(nrows=5,ncols=2,figsize=(20,20))
fig.suptitle('Incomplete Data Set')

for row in ax:
    for col in row:
        col.bar(df[x],df[y[i]])
        i=i+1
i=0
for ax in fig.axes:
    plt.xlabel('States')
    plt.ylabel("no of people affected")
    plt.title(z[i])
    i=i+1
    plt.sca(ax)
    plt.xticks(rotation=90)
    plt.grid()
    plt.subplots_adjust(left=None, bottom=None, right=None, top=None, wspace=None, hspace=1)

fig.tight_layout()
fig.subplots_adjust(top=0.95)
plt.savefig('bar_incomplete.png',bbox_inches='tight')

############

i=1
fig,ax=plt.subplots(nrows=5,ncols=2,figsize=(20,20))
fig.suptitle('NaN Filled Data Set')

for row in ax:
    for col in row:
        col.bar(bdf[x],bdf[y[i]])
        i=i+1
i=0
for ax in fig.axes:
    plt.xlabel('States')
    plt.ylabel("no of people affected")
    plt.title(z[i])
    i=i+1
    plt.sca(ax)
    plt.xticks(rotation=90)
    plt.grid()
    plt.subplots_adjust(left=None, bottom=None, right=None, top=None, wspace=None, hspace=1)

fig.tight_layout()
fig.subplots_adjust(top=0.95)
plt.savefig('bar_complete.png',bbox_inches='tight')

y=list(df.columns)
usa=df.copy()
for col in range(1,len(y)):
    usa[y[col]].fillna((usa[y[col]].mean()), inplace=True)

usa['total']=usa.sum(axis=1)
states = ["AL", "AK", "AZ", "AR", "CA", "CO", "CT", "DC", "DE", "FL", "GA", 
          "HI", "ID", "IL", "IN", "IA", "KS", "KY", "LA", "ME", "MD", 
          "MA", "MI", "MN", "MS", "MO", "MT", "NE", "NV", "NH", "NJ", 
          "NM", "NY", "NC", "ND", "OH", "OK", "OR", "PA", "RI", "SC", 
          "SD", "TN", "TX", "UT", "VT", "VA", "WA", "WV", "WI", "WY"]
usa['code']=states
for col in usa.columns:
    usa[col] = usa[col].astype(str)

scl = [[0.0, 'rgb(242,240,247)'],[0.2, 'rgb(218,218,235)'],[0.4, 'rgb(188,189,220)'],\
            [0.6, 'rgb(158,154,200)'],[0.8, 'rgb(117,107,177)'],[1.0, 'rgb(84,39,143)']]

usa['text'] = usa['State'] + '<br>' +\
    'Brain/nervoussystem '+usa['Brain/nervoussystem']+' Femalebreast '+usa['Femalebreast']+'<br>'+\
    'Colon&rectum '+usa['Colon&rectum']+' Leukemia ' + usa['Leukemia']+'<br>'+\
    'Liver '+usa['Liver']+' Lungs&bronchus ' + usa['Lung&bronchus']+'<br>'+\
    'Non-HodgkinLymphoma '+usa['Non-HodgkinLymphoma']+' Ovary ' + usa['Ovary']+'<br>'+\
    'Pancreas '+usa['Pancreas']+' Prostate ' + usa['Prostate']
    

data = [ dict(
        type='choropleth',
        colorscale = scl,
        autocolorscale = False,
        locations = usa['code'],
        z = usa['total'].astype(float),
        locationmode = 'USA-states',
        text = usa['text'],
        marker = dict(
            line = dict (
                color = 'rgb(255,255,255)',
                width = 2
            ) ),
        colorbar = dict(
            title = "No of People")
        ) ]

layout = dict(
        title = '2017 Cancer Statistics of U.S.A<br>(Hover for breakdown)',
        geo = dict(
            scope='usa',
            projection=dict( type='albers usa' ),
            showlakes = True,
            lakecolor = 'rgb(255, 255, 255)'),
             )
    
fig = dict( data=data, layout=layout )
py.plot( fig, filename='d3-cloropleth-map' )
py.image.save_as(fig, filename='cancer_usa.png')

   
#m = Basemap(llcrnrlon=-119,llcrnrlat=22,urcrnrlon=-64,urcrnrlat=49,
#        projection='lcc',lat_1=32,lat_2=45,lon_0=-95)


## load the shapefile, use the name 'states'
#m.readshapefile('st99_d00', name='states', drawbounds=True)
#
#
## Get the location of each city and plot it
#geolocator = Nominatim()
#x, y = map(0, 0)
#
#m.plot(x, y, marker='D',color='m')



#
#scl = [[0.0, 'rgb(242,240,247)'],[0.2, 'rgb(218,218,235)'],[0.4, 'rgb(188,189,220)'],\
#            [0.6, 'rgb(158,154,200)'],[0.8, 'rgb(117,107,177)'],[1.0, 'rgb(84,39,143)']]
#
#
#
#data = [ dict(
#        type='choropleth',
#        colorscale = scl,
#        autocolorscale = False,
#        locationmode = 'USA-states',
#        marker = dict(
#            line = dict (
#                color = 'rgb(255,255,255)',
#                width = 2
#            )
#        ),
#        colorbar = dict(
#            title = "Millions USD"
#        )
#    ) ]
#
#layout = dict(
#        title = '2011 US Agriculture Exports by State<br>(Hover for breakdown)',
#        geo = dict(
#            scope='usa',
#            projection=dict( type='albers usa' ),
#            showlakes = True,
#            lakecolor = 'rgb(255, 255, 255)',
#        ),
#    )
#
#fig = dict(data=data, layout=layout)
#
#url = py.plot(fig, filename='d3-cloropleth-map')
#install geopandas shapely in anaconda prompt
#conda install -c conda-forge fiona shapely pyproj rtree
#conda install pandas

#writer = pd.ExcelWriter('pandas_simple.xlsx', engine='xlsxwriter')
#df.to_excel(writer, sheet_name='Sheet1')
#writer.save()


#with open('cancer2017.csv', 'rb') as f:
#     lines = [l.decode('utf8', 'ignore') for l in f.readlines()]
#data=[]
#for i in lines:
#    lis=i.split(',')
#    
#    data.append(lis)
#df=pd.DataFrame(data)
#print(df)


#col=lines[0].split(',')
#data.columns=data.iloc[0]
#print(data.columns)