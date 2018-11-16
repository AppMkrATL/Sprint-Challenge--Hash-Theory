def get_indices_of_item_weights(weights, limit):
  weight_table = {}
  result = ()
  if len(weights) == 2:
    if (weights[0] + weights[1] == limit):
      print((1,0))
      return (1,0)
  
  for index, w in enumerate(weights):
    weight_table[w] = index #assigns key to weight, value to list index
  for k,v in weight_table.items(): #prints list of key/value pairs
    print(k, ':', v)
    if ((limit - weights[v]) in weight_table):
      print('success')
      result = result + (v,)
  print(tuple(sorted(result,reverse=True)))    
  return tuple(sorted(result,reverse=True))



if __name__ == '__main__':
  # You can write code here to test your implementation using the Python repl
  # get_indices_of_item_weights([4, 6, 10, 15, 16], 21)
  get_indices_of_item_weights([4, 4], 8)
