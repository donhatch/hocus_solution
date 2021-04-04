#!/usr/bin/python3

# Solving the "hocus" android game.

# Input #43:
#       *
#      /|
#     * |
#    /| |
#   * | |
#   |\| |
#   | * |
#   | |\|
#   | | *
#   | | |
#   | | *
#   | |/
#   | *
#   |/
#   *

#
# Simplest input:
#       *
#      /|
#     * |
#      \|
#       *

# Simplest intermediate:

#                             *
#                            / \
#                           /   *
#                          /   /|
#                         /   / |
#                        /   /  |
#                       /   / * |
#                      /   / /| |
#                     /   / / | |
#                    /   / /| | |
#                   /   / / | | |
#                  *   * /  | | |
#                  |\   \   | | |
#                  * \   \  | | |
#                   \ \   \ | | |
#                    \ \   \| | |
#                     \ \   | | |
#                      \ \  | | |
#                       \ \ | | |
#                        \ \| | |
#                         \ * | |
#                          \  | |
#                           \ | *
#                            \|/
#                             *  
#                             *
#                            / \
#                           /   *
#                          /   /|
#                         /   / |
#                        /   /  |
#                       /   / * |
#                      /   / /| |
#                     /   / / | |
#                    /   / /| | |
#                   *   * / | | |
#                   |\   \  | | |
#                   * \   \ | | |
#                    \ \   \| | |
#                     \ \   | | |
#                      \ \  | | |
#                       \ \ | | |
#                        \ \| | |
#                         \ * | |
#                          \  | |
#                           \ | *
#                            \|/
#                             *  
#                             *
#                            / \
#                           /   *
#                          /   /|
#                         /   / |
#                        /   /  |
#                       /   / * |
#                      /   / /| |
#                     /   / / | |
#                    *   * /| | |
#                    |\   \ | | |
#                    * \   \| | |
#                     \ \   | | |
#                      \ \  | | |
#                       \ \ | | |
#                        \ \| | |
#                         \ * | |
#                          \  | |
#                           \ | *
#                            \|/
#                             *  
#                             *
#                            / \
#                           /   *
#                          /   /|
#                         /   / |
#                        /   /  |
#                       /   / * |
#                      /   / /| |
#                     *   * / | |
#                     |\   \| | |
#                     * \   | | |
#                      \ \  | | |
#                       \ \ | | |
#                        \ \| | |
#                         \ * | |
#                          \  | |
#                           \ | *
#                            \|/
#                             *  




namesAndInputs = [
  ['intput1', [
    '  *',
    ' / ',
    '*  ',
  ]],
  ['input2', [
    '  *',
    '  |',
    '* *',
    '|/ ',
    '*  ',
  ]],
  ['input3', [
    '*   *  ',
    ' \ / \ ',
    '  /   *',
    ' / \ / ',
    '*   *  ',
  ]],
  ['input4', [
    '*  ',
    '|\ ',
    '| *',
    '|/ ',
    '*  ',
  ]],
  ['input5', [
    '  *',
    ' /|',
    '* |',
    '| |',
    '* |',
    ' \|',
    '  *',
  ]],
  ['input6', [
    '  *  ',
    ' /|\ ',
    '* | *',
    '| | |',
    '* | *',
    ' \|/ ',
    '  *  ',
  ]],
  ['input7', [
    '      *',
    '     /|',
    '    / |',
    '   /  |',
    '  *   *',
    ' / \ /|',
    '*   * |',
    ' \  | |',
    '  \ | |',
    '   \| |',
    '    * |',
    '     \|',
    '      *',
  ]],
  ['input8', [
    '*    ',
    ' \   ',
    '  *  ',
    ' / \ ',
    '*   *',
    '|\ / ',
    '| *  ',
    '|/   ',
    '*    ',
  ]],
  ['input9', [
    '*   *',
    '|\ /|',
    '| \ |',
    '|/ \|',
    '*   *',
  ]],
  ['input10', [
    '    *  ',
    '    |  ',
    '  * | *',
    '  | |/|',
    '  | | *',
    '  |/|/ ',
    '  | / *',
    ' /|/|/ ',
    '* / |  ',
    ' /|/|  ',
    '* | |  ',
    '|/| |  ',
    '* | *  ',
    '  |    ',
    '  *    ',
  ]],
  ['input11', [
    '  *  ',
    ' / \ ',
    '*   *',
    '|\ /|',
    '| * |',
    '|/| |',
    '* | *',
    ' \|/ ',
    '  *  ',
  ]],
  ['input12', [
    '    *',
    '   /|',
    '  * |',
    '  | |',
    '  | *',
    '  |/ ',
    '  |  ',
    ' /|  ',
    '* | *',
    '| |/|',
    '| / |',
    '|/| |',
    '* | *',
    '  |/ ',
    '  *  ',
  ]],
  ['input13', [
    '  *  ',
    ' /|\ ',
    '* | *',
    '|\|/|',
    '| * |',
    '|/|\|',
    '* | *',
    ' \|/ ',
    '  *  ',
  ]],
  ['input14', [
    '  *  ',
    ' / \ ',
    '*   *',
    '|\ /|',
    '| / |',
    '|/ \|',
    '*   *',
    ' \ / ',
    '  *  ',
  ]],
  ['input15', [
    '  *  ',
    ' / \ ',
    '*   *',
    ' \ / ',
    '  /  ',
    ' / \ ',
    '*   *',
    ' \ / ',
    '  /  ',
    ' / \ ',
    '*   *',
    ' \ / ',
    '  *  ',
  ]],
  ['input16', [
    '  *    ',
    '  |\   ',
    '* | \  ',
    '|\|  \ ',
    '| *   *',
    '| |\ / ',
    '| | *  ',
    '| |/ \ ',
    '| *   *',
    '|    / ',
    '|   /  ',
    '|  /   ',
    '| /    ',
    '|/     ',
    '*      ',
  ]],
  ['input17', [
    '    *  ',
    '    |\ ',
    '    | *',
    '    |/ ',
    '*   |  ',
    '|\ /|  ',
    '| / |  ',
    '|/ \|  ',
    '*   |  ',
    '    |\ ',
    '    | *',
    '    |/ ',
    '    *  ',
  ]],
  ['input18', [
    '      *',
    '     /|',
    '    / |',
    '   /  |',
    '  /   *',
    ' /   /|',
    '*   * |',
    ' \ /| |',
    '  * | |',
    '   \| |',
    '    * |',
    '     \|',
    '      *',
  ]],
  ['input19', [
    '      *  ',
    '     /|  ',
    '    / |  ',
    '   /  |  ',
    '  *   *  ',
    ' / \ /|  ',
    '*   * | *',
    '|  /| |/|',
    '| / | | |',
    '|/  |/| |',
    '*   * | *',
    '|  /  |/ ',
    '| /   *  ',
    '|/       ',
    '*        ',
  ]],
  ['input20', [
    '    *  ',
    '   /|  ',
    '  / | *',
    ' /  |/|',
    '*   | |',
    '|  /| |',
    '| * | |',
    '|  \| |',
    '*   \ |',
    ' \  |\|',
    '  \ | *',
    '   \|  ',
    '    *  ',
  ]],
  #['input21', [
  #]],
  #['input22', [
  #]],
  ['input23', [
    '    *  ',
    '   /|\ ',
    '  / | *',
    ' /  |/|',
    '*   / |',
    '|\ /| |',
    '| * | |',
    '| | | |',
    '| | * |',
    '| |/ \|',
    '| |   *',
    '|/|  / ',
    '* | /  ',
    ' \|/   ',
    '  *    ',
  ]],
  # ...
  ['input43', [
    '    *',
    '   /|',
    '  * |',
    ' /| |',
    '* | |',
    '|\| |',
    '| * |',
    '| |\|',
    '| | *',
    '| | |',
    '| | *',
    '| |/ ',
    '| *  ',
    '|/   ',
    '*    ',
  ]],
]  # namesAndInputs

def makePicture(nodes, node2index, edges, roominess):
  print("        in makePicture")
  # If input was this:
  #       *
  #      /|
  #     * |
  #      \|
  #       *
  # Roominess=1:
  #                             *
  #                            / \
  #                           /   *
  #                          /   /|
  #                         /   / |
  #                        /   /  |
  #                       /   / * |
  #                      /   / /| |
  #                     /   / / | |
  #                    *   * /| | |
  #                    |\   \ | | |
  #                    * \   \| | |
  #                     \ \   | | |
  #                      \ \  | | |
  #                       \ \ | | |
  #                        \ \| | |
  #                         \ * | |
  #                          \  | |
  #                           \ | *
  #                            \|/
  #                             *  
  # Roominess=0:
  #                             *
  #                            / \
  #                           /   *
  #                          /   /|
  #                         /   / |
  #                        /   /  |
  #                       /   / * |
  #                      /   / /| |
  #                     *   * / | |
  #                     |\   \| | |
  #                     * \   | | |
  #                      \ \  | | |
  #                       \ \ | | |
  #                        \ \| | |
  #                         \ * | |
  #                          \  | |
  #                           \ | *
  #                            \|/
  #                             *  

  minrow = min(irow for (irow,icol) in nodes)
  maxrow = max(irow for (irow,icol) in nodes)
  print("          minrow = %r" % (minrow,))
  print("          maxrow = %r" % (maxrow,))

  # maxrow-minrow = 0: 9 rows of output
  #     *
  #    / \
  #   *   *
  #   |\ /|
  #   | * |
  #   | | |
  #   * | *
  #    \|/
  #     *
  # If roominess is 0, there 8 more output rows for every additional input row.
  # If roominess is 1, there are 9 more. etc.
  n_rows_out = 9 + (maxrow-minrow) * (8+roominess)
  print("          n_rows_out = %r" % (maxrow,))


  print("        out makePicture")

def process(name, input, roominess):
  print("    in process(name="+name+")")
  assert len(input) > 0
  assert len(set([len(line) for line in input])) == 1, "hey! inputs don't have all the same lengths"
  
  # Find the nodes (positions)
  nodes = []
  for irow in range(len(input)):
    for icol in range(len(input[irow])):
      assert input[irow][icol] in ' *|/\\'
      if input[irow][icol] == '*':
        nodes.append((irow,icol))
  print("      nodes = %r" % (nodes,))

  node2index = dict(((nodes[i],i) for i in range(len(nodes))))
  print("      node2index = %r" % (node2index,))

  # Find the edges (pairs of indices into nodes).
  # If this gets an out-of-bounds exception, it means input was bogus.
  edges = set()
  for irow in range(len(input)):
    for icol in range(len(input[irow])):
      if input[irow][icol] == '|':
        delta = (1,0)
      elif input[irow][icol] == '/':
        delta = (1,-1)
      elif input[irow][icol] == '\\':
        delta = (1,1)
      else:
        continue
      jrow0,jcol0 = irow,icol
      while input[jrow0][jcol0] != '*':
        jrow0 -= delta[0]
        jcol0 -= delta[1]
      jrow1,jcol1 = irow,icol
      while input[jrow1][jcol1] != '*':
        jrow1 += delta[0]
        jcol1 += delta[1]
      edges.add((node2index[(jrow0,jcol0)], node2index[(jrow1,jcol1)]))
  print("      edges = %r" % (edges,))

  picture = makePicture(nodes, node2index, edges, roominess)

  print("    out process(name="+name+")")

roominess = 1  # XXX input
for name,input in namesAndInputs:
  process(name, input, roominess)


