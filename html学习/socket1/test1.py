import time

str123 = """
<h1 style='background-color:red;'>@@@@@<h1>
<a href='http://www.oldboyedu.com'>go</a>
<table border='1'>
    <tr>
        <td>1</td>
        <td>2</td>
        <td>3</td>
    </tr>
    <tr>
        <td>1</td>
        <td>2</td>
        <td>3</td>
    </tr>
<table>
"""
r = time.time()
r = str(r)
print r
print str123.replace("@@@@@",r)