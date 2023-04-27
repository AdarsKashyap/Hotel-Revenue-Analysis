#!/usr/bin/env python
# coding: utf-8

# In[6]:


import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
df=pd.read_csv('C:\\Users\\hp\\OneDrive\\Desktop\\datasets\\hotel_bookings 2.csv')
df


# In[ ]:


for i in df.columns:
    value_counts = df[i].value_counts(normalize=True)*100
    print(f"Unique value count in percentage for {i}:")
    print(value_counts)
    plt.figure(figsize=(2,2))
    plt.bar(value_counts.index.astype(str), value_counts.values)
    plt.title(f"Percentage of unique values in {i}")
    plt.xlabel(i)
    plt.ylabel("Percentage")
    plt.show()


# In[4]:


df['reservation_status_date']=pd.to_datetime(df['reservation_status_date'])


# In[5]:


df.describe(include='object')


# In[6]:



for column in df.describe(include='object').columns:
    print(column)
    print(df[column].unique())
    print('__'*25)


# In[7]:


df.isnull().sum()


# In[8]:


df.drop(['agent','company'],axis=1,inplace=True)
df.dropna(inplace=True)


# In[ ]:


for i in df.columns:
    value_counts = df[i].value_counts(normalize=True)*100
    print(f"Unique value count in percentage for {i}:")
    print(value_counts)
    plt.figure(figsize=(2,2))
    plt.bar(value_counts.index.astype(str), value_counts.values)
    plt.title(f"Percentage of unique values in {i}")
    plt.xlabel(i)
    plt.ylabel("Percentage")
    plt.show()


# In[ ]:


df=df[df['adr']<5000]


# In[ ]:


a=df['is_canceled'].value_counts(normalize=True)
a


# In[ ]:


plt.figure(figsize=(5,4))
plt.title('reservation status count')
plt.bar(['not cancelled','canclled'],df['is_canceled'].value_counts(),edgecolor='k',width=0.4)
plt.show()


# In[ ]:


plt.figure(figsize=(8,4))
O=sns.countplot(x='hotel',hue='is_canceled',data=df,palette='Reds')
plt.title('Reservation status in hotel')
plt.xlabel('hotel')
plt.ylabel('number of reservations')
plt.legend(['not cancelled','cancelled'])
plt.show()


# In[ ]:


Resort=df[df['hotel']=='Resort Hotel']
Resort['is_canceled'].value_counts(normalize=True)


# In[ ]:


City=df[df['hotel']=='City Hotel']
City['is_canceled'].value_counts(normalize=True)


# In[ ]:


Resort=Resort.groupby('reservation_status_date')[['adr']].mean()
City=City.groupby('reservation_status_date')[['adr']].mean()


# In[ ]:


#ADR VISUALISATION
plt.figure(figsize=(10,5))
plt.title('Average daily rate')
plt.plot(Resort.index,Resort['adr'],label='Resort Hotel')
plt.plot(City.index,City['adr'],label='City Hotel')
plt.legend()
plt.show()


# In[ ]:


df['month']=df['reservation_status_date'].dt.month
plt.figure(figsize=(8,4))
O=sns.countplot(x='month',hue='is_canceled',data=df,palette='Purples')
plt.title('Monthly Reservation')
plt.xlabel('month')
plt.ylabel('number of reservations')
plt.legend(['not cancelled','cancelled'])
plt.show()


# In[ ]:


plt.figure(figsize=(15,9))
#O=sns.countplot(x='month',hue='is_canceled',data=df,palette='Purples')
plt.title('AVERAGE DAILY RATE Per month',fontsize=28)
sns.barplot('month','adr',data=df[df['is_canceled']==1].groupby('month')[['adr']].sum().reset_index())
plt.show()


# In[ ]:


Cancelled_data=df[df['is_canceled']==1]
Country=Cancelled_data['country'].value_counts()[:12]
plt.figure(figsize=(10,10))
plt.pie(Country, labels=Country.index,autopct='%.2f')
plt.title('Top 12 country with cancelled reservation')

plt.show()

