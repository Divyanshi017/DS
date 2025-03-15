book={}
book['tom']= {
    'name' : 'tom',
    'address' : 'raippur',
    'phone' : '4454676586334'
}
book['bob']= {
    'name' : 'bob',
    'address' : 'rajpur',
    'phone' : '87754586334'
}

import json
s=json.dumps(book)
print(s)