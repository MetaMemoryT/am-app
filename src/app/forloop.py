import re

template = """
<table>
  {for e in items}
    <tr>
      <td> {e} </td>
    </tr>
  {end for}
</table>
"""

def installFor(t,l):
    m = re.search("{for.+\n",t)
    header = t[0:m.start()]
    rest = t[m.end():]
    m2 = re.search("\{end for\}", rest)
    #print(m.end())
    inner = rest[0:m2.start()]
    #print(header)
    #print(rest)
    #print(inner)
    footer = rest[m2.end():]
    #print(footer)
    t2 = header
    for e in l:
        t2 += re.sub("{e}", e, inner)
    t2+=footer
    return t2

t = installFor(template, ["a","b","c"])
print(t)