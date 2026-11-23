with open('/Users/green/Downloads/Takealot PlayStation 5/track.html', 'r', encoding='utf-8') as f:
    c = f.read()

c = c.replace('TAK-70-189210 (432L)', 'TAK-70-189210 (2TB Pro)')
c = c.replace('TAK-20-883910 (254L)', 'TAK-20-883910 (1TB Digital)')
c = c.replace('Capacity: ${order.screen_size', 'Edition: ${order.screen_size')

with open('/Users/green/Downloads/Takealot PlayStation 5/track.html', 'w', encoding='utf-8') as f:
    f.write(c)

print('Polished track.html!')
