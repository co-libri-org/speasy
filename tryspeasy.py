import sys
from pprint import pprint

import speasy as spz
from speasy import amda, ssc
from speasy.core.http import urlopen

# from speasy import cdpp3dview
# from speasy import data_providers
from speasy.data_providers import Cdpp3dViewWebservice, SscWebservice

# spz.config.core.disabled_providers.set("cdpp3dview")
spz.config.core.disabled_providers.set("")

# choice: str = "cdpp_inventory"
choice: str = "ssc_param_names"
choice: str = "cdpp_param_names"
if choice == "cdpp_indexes":
    cdpp3dview_bodies = spz.inventories.data_tree.cdpp3dview.Bodies
    print(cdpp3dview_bodies.spz_name())
    cdpp3dview_frames = spz.inventories.data_tree.cdpp3dview.Frames
    print(cdpp3dview_frames.spz_name())
    sys.exit()
elif choice == "cdpp_inventory":
    """ output:

        {'Bodies': <SpeasyIndex: Bodies>,
        'Frames': <SpeasyIndex: Frames>,
        '__spz_name__': 'root',
        '__spz_provider__': 'cdpp3dview',
        '__spz_type__': 'SpeasyIndex',
        '__spz_uid__': 'root'}
    """
    cdppws = Cdpp3dViewWebservice()
    inventory = cdppws.build_inventory(
        spz.SpeasyIndex(name="root", provider="cdpp3dview", uid="root")
    )
    pprint(inventory.__dict__)
    sys.exit()
elif choice == "ssc_inventory":
    """ output:

        {'Trajectories': <SpeasyIndex: Trajectories>,
        '__spz_name__': 'root',
        '__spz_provider__': 'sscws',
        '__spz_type__': 'SpeasyIndex',
        '__spz_uid__': 'root'}
    """
    sscws = SscWebservice()
    inventory = sscws.build_inventory(
        spz.SpeasyIndex(name="root", provider="sscws", uid="root")
    )
    pprint(inventory.__dict__)
    sys.exit()
elif choice == "cdpp_bodies_json":
    URL = "https://3dview.irap.omp.eu/webresources/get_bodies"
    with urlopen(URL, headers={"Accept": "application/json"}) as response:
        data = response.json()
    pprint(data)
    sys.exit()
elif choice == "ssc_get_data":
    ssc_ssc_param = ssc.get_data("ace", "2022-07-30", "2022-08-01")
    ssc_ssc_df = ssc_ssc_param.to_dataframe()
    print(ssc_ssc_df.head())
    sys.exit()
elif choice == "amda_get_data":
    amda_tree = spz.inventories.tree.amda
    ace_mag = spz.get_data(
        amda_tree.Parameters.ACE.MFI.ace_imf_all.imf, "2016-6-2", "2016-6-5"
    )
    sys.exit()
elif choice == "cdpp_param_names":
    # print(ssc_trajectories.spz_name())
    # print(ssc_trajectories.spz_provider())
    # print(ssc_trajectories.spz_type())
    # print(ssc_trajectories.spz_uid())
    # # print(ssc_tree.Trajectories)
    print(list(spz.inventories.flat_inventories.cdpp3dview.parameters.keys()))
    print(
        list(spz.inventories.flat_inventories.cdpp3dview.parameters.values())
    )
    sys.exit()
elif choice == "ssc_param_names":
    """ output:

        Trajectories
        ssc
        SpeasyIndex
        Trajectories
        ['ace', 'active', 'adityal1', 'aec', 'aed', 'aee', 'aerocube6a', 'aerocube6b', 'aim', 'akebono']
    """
    # ssc_trajectories = spz.inventories.data_tree.ssc.Trajectories
    # print(ssc_trajectories.spz_name())
    # print(ssc_trajectories.spz_provider())
    # print(ssc_trajectories.spz_type())
    # print(ssc_trajectories.spz_uid())
    # print(ssc_tree.Trajectories)
    ssc_trajectories = spz.inventories.data_tree.ssc.Trajectories
    print(list(spz.inventories.flat_inventories.ssc.parameters.keys())[:10])
    sys.exit()
else:
    sys.exit()

# print(type(cdpp3dview.Cdpp3dViewWebservice))
# print(type(cdpp3dview))

# print(type(amda))
# print(type(amda.AmdaWebservice()))


# spz.update_inventories()
# print(spz.config.core.disabled_providers.get())
# print(spz.data_providers)

# print(spz.inventories.flat_inventories.amda)
# print(amda_tree)
# print(type(spz.inventories.tree.amda.Parameters.Wind.SWE.wnd_swe_kp.wnd_swe_n))

# spz.inventories.data_tree.Cdpp3dViewWebservice

# cdpp3 = Cdpp3dViewWebservice()
# bodies = cdpp3._get_bodies()
# frames = cdpp3._get_frames()
# pprint(bodies[:3])
# pprint(frames[:3])

# # sscws = spz.data_providers.get_provider('sscweb')
# obs = sscws.get_observatories()
#   for o in obs[:5]:
#      pprint(o)
#   pprint(obs[:3])
#   pprint(obs)
# inv = list(map(make_index, obs[1:2]))
#   for p in inv:
#       print(p)
