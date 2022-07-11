def apartmentHunting(blocks,reqs):
    avail=[[index for index,block in enumerate(blocks)if block[building]] for building in reqs]
    distance=[max(min((abs(i-ele)) for ele in item) for item in avail) for i in range(len(blocks))]
    optimumblock=distance.index(min(distance))
    maxdistance=distance[optimumblock]
    return optimumblock,maxdistance

blocks=[{'gym': False, 'office': False, 'school': True, 'store': False}, 
        {'gym': True, 'office': True, 'school': False, 'store': False}, 
        {'gym': False, 'office': False, 'school': True, 'store': False}, 
        {'gym': False, 'office': False, 'school': True, 'store': False}, 
        {'gym': True, 'office': True, 'school': True, 'store': False}, 
        {'gym': True, 'office': True, 'school': False, 'store': False}, 
        {'gym': False, 'office': False, 'school': False, 'store': True}]

reqs=['gym', 'office', 'school', 'store']

optimumblock,maxdistance=apartmentHunting(blocks,reqs)
print('{}, At block with index {}, the farthest you would have to walk to reach any of the required building is {}; at any other index, you would have to walk farther.'.format(optimumblock,optimumblock,maxdistance))
