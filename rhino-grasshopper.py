import compute_rhino3d
import compute_rhino3d.Util
import compute_rhino3d.Curve
import compute_rhino3d.Brep  
import base64

compute_rhino3d.Util.authToken = "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJwIjoiUEtDUyM3IiwiYyI6IkFFU18yNTZfQ0JDIiwiYjY0aXYiOiJGSzVQK3FoT2Q2NDQ3SDVBMkp2QXZ3PT0iLCJiNjRjdCI6InhyT3l4aXowa01uczdxU3p5YUo3Slo4ZUU5ekYrYm9rTlJMdThseXdRNkpzb0lwQjZwcXpPZ3lyQitZUXQxT0h3Z2pTMUJPWlhFaGNVYmRBdjJTZDN2czhudUZYSVlidFRVdjFnUGRyN1F3b2p6emZYYVQrUld1SDV5bXBQL3ZTdTUxcjZkUkZFM1VmQUo3NHF4OWoyNHhjUEdTQ0MrMG51QzlwVUhMMlhKRVN1UWVkdVQwZG9GZUoyRGxOalN3WDlmYVlSOUtGSHcyV2k4M2xCODJ1SlE9PSIsImlhdCI6MTYyMTYxMTU5M30.M4op1S4A-YrIvEgjqA8UgJxPVgLWPY-jC8ssl4qokcQ"
print("ugur")


brace_gen_path = "/home/ugur/Desktop/befited_design/Brace_Generator_Resources/2021_03_11_Brace_Generation_Script.gh"
#gh_data = open("./voronoi.ghx", mode="r", encoding="utf-8-sig").read()
gh_data = open(brace_gen_path, mode="rb", encoding="utf-8-sig").read()
print(gh_data)
#gh_data = open(brace_gen_path, mode="r", encoding="utf-8-sig").read()
data_bytes = gh_data.encode("utf-8")
encoded = base64.b64encode(data_bytes)
decoded = encoded.decode("utf-8")

