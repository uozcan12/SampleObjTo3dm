import compute_rhino3d.Util
import compute_rhino3d.Grasshopper as gh
import rhino3dm
import json

compute_rhino3d.Util.authToken = "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJwIjoiUEtDUyM3IiwiYyI6IkFFU18yNTZfQ0JDIiwiYjY0aXYiOiJGSzVQK3FoT2Q2NDQ3SDVBMkp2QXZ3PT0iLCJiNjRjdCI6InhyT3l4aXowa01uczdxU3p5YUo3Slo4ZUU5ekYrYm9rTlJMdThseXdRNkpzb0lwQjZwcXpPZ3lyQitZUXQxT0h3Z2pTMUJPWlhFaGNVYmRBdjJTZDN2czhudUZYSVlidFRVdjFnUGRyN1F3b2p6emZYYVQrUld1SDV5bXBQL3ZTdTUxcjZkUkZFM1VmQUo3NHF4OWoyNHhjUEdTQ0MrMG51QzlwVUhMMlhKRVN1UWVkdVQwZG9GZUoyRGxOalN3WDlmYVlSOUtGSHcyV2k4M2xCODJ1SlE9PSIsImlhdCI6MTYyMTYxMTU5M30.M4op1S4A-YrIvEgjqA8UgJxPVgLWPY-jC8ssl4qokcQ"

pt1 = rhino3dm.Point3d(0, 0, 0)
circle = rhino3dm.Circle(pt1, 5)
angle = 20

# convert circle to curve and stringify
curve = json.dumps(circle.ToNurbsCurve().Encode())

# create list of input trees
curve_tree = gh.DataTree("RH_IN:curve")
curve_tree.Append([0], [curve])
rotate_tree = gh.DataTree("RH_IN:rotate")
rotate_tree.Append([0], [angle])
trees = [curve_tree, rotate_tree]

output = gh.EvaluateDefinition('twisty.gh', trees)
# print(output)

# decode results
branch = output['values'][0]['InnerTree']['{ 0; }']
lines = [rhino3dm.CommonObject.Decode(json.loads(item['data'])) for item in branch]

filename = 'twisty.3dm'

print('Writing {} lines to {}'.format(len(lines), filename))

# create a 3dm file with results
model = rhino3dm.File3dm()
for l in lines:
    model.Objects.AddCurve(l) # they're actually LineCurves...

model.Write(filename)