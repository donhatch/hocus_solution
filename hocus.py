#!/usr/bin/python3

# Solving the "hocus" android game.

import sys

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
  ['trivial', [
    '*',
  ]],
  ['canonical2', [
    '*    ',
    '|\   ',
    '| *  ',
    '|/|\ ',
    '* | *',
    '|\|/ ',
    '| *  ',
    '|/   ',
    '*    ',
  ]],
  ['input1', [
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
  ['input21', [
    '  *    ',
    '  |\   ',
    '* | \  ',
    ' \|  \ ',
    '  |   *',
    '  |\  |',
    '* | * |',
    ' \| | |',
    '  \ | |',
    '  |\| |',
    '  | | |',
    '  | |\|',
    '  * | *',
    '   \|  ',
    '    *  ',
  ]],
  ['input22', [
    '      *',
    '     /|',
    '    * |',
    '    | |',
    '    | *',
    '    |/|',
    '    | |',
    '   /| |',
    '  * | |',
    ' / \| |',
    '*   \ |',
    ' \  |\|',
    '  \ | *',
    '   \|  ',
    '    *  ',
  ]],
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
  ['input24', [
    '    *    ',
    '   / \   ',
    '  /   \  ',
    ' /     \ ',
    '*   *   *',
    '|\ / \ /|',
    '| \   \ |',
    '|/ \ / \|',
    '*   *   *',
    ' \     / ',
    '  \   /  ',
    '   \ /   ',
    '    *    ',
  ]],
  ['input25', [
    '    *    ',
    '   /|\   ',
    '  * | *  ',
    ' /| | |\ ',
    '* | | | *',
    ' \| | |/ ',
    '  * | *  ',
    '   \|/   ',
    '    *    ',
  ]],
  ['input26', [
    '*    ',
    '|\   ',
    '| *  ',
    '| |\ ',
    '| | *',
    '| |/|',
    '| * |',
    '|/| |',
    '* | |',
    ' \| |',
    '  * |',
    '   \|',
    '    *',
  ]],
  ['input27', [
    '  *    ',
    ' /|\   ',
    '* | *  ',
    ' \| |\ ',
    '  * | *',
    '   \|/ ',
    '    *  ',
  ]],
  ['input28', [
    '*  ',
    '|\ ',
    '| *',
    '|/|',
    '* |',
    '| |',
    '| *',
    '|/|',
    '* |',
    '| |',
    '| |',
    '| |',
    '* |',
    ' \|',
    '  *',
  ]],
  ['input29', [
    '  *   *',
    '  |  /|',
    '  | * |',
    '  |/| |',
    '  | | *',
    ' /| |/ ',
    '* | |  ',
    '| |/|  ',
    '| * |  ',
    '|/  |  ',
    '*   *  ',
  ]],
  ['input30', [
    '    *  ',
    '   /|  ',
    '  / |  ',
    ' /  |  ',
    '*   *  ',
    '|\ /|  ',
    '| * | *',
    '| | |/ ',
    '| | /  ',
    '| |/|  ',
    '| | |  ',
    '|/| |  ',
    '* | *  ',
    '  |/   ',
    '  *    ',
  ]],
  ['input31', [
    '*       *',
    ' \     /|',
    '  \   / |',
    '   \ /  |',
    '*   \   *',
    ' \ / \ / ',
    '  /   /  ',
    ' / \ / \ ',
    '*   *   *',
    '   / \  |',
    '  /   \ |',
    ' /     \|',
    '*       *',
  ]],
  ['input32', [
    '  *  ',
    ' /|  ',
    '* |  ',
    ' \|  ',
    '  \  ',
    '  |\ ',
    '  | *',
    '  | |',
    '  | |',
    '  | |',
    '  | *',
    '  |/ ',
    '  |  ',
    ' /|  ',
    '* |  ',
    '| |  ',
    '| *  ',
    '|/   ',
    '*    ',
  ]], 
  ['input33', [
    '    *   *  ',
    '   /|\ / \ ',
    '  / | *   *',
    ' /  | |  / ',
    '*   | | /  ',
    ' \  | |/   ',
    '  * | /    ',
    '  |\|/|    ',
    '  | * |    ',
    '  | | |    ',
    '  | | *    ',
    '  | |/     ',
    '  | *      ',
    '  |/       ',
    '  *        ',
  ]], 
  ['input34', [
    '    *    ',
    '   /|\   ',
    '  / | \  ',
    ' /  |  \ ',
    '*   |   *',
    '|\  |  /|',
    '| * | * |',
    '|/  |  \|',
    '*   |   *',
    ' \  |  / ',
    '  \ | /  ',
    '   \|/   ',
    '    *    ',
  ]], 
  ['input35', [
    '    *  ',
    '   /|\ ',
    '  / | *',
    ' /  |/|',
    '*   / |',
    '|\ /| |',
    '| * | |',
    '| | | |',
    '| | | |',
    '| | | |',
    '| * | |',
    '|/ \| |',
    '*   | |',
    ' \  |\|',
    '  \ | *',
    '   \|/ ',
    '    *  ',
  ]], 
  ['input36', [
    '    *  ',
    '   /|  ',
    '  / | *',
    ' /  |/|',
    '*   * |',
    ' \ /| |',
    '  \ | |',
    ' / \| |',
    '*   | |',
    ' \  |\|',
    '  \ | *',
    '   \|  ',
    '    *  ',
  ]], 
  ['input37', [
    '  *      ',
    '  |\     ',
    '  | *    ',
    '  |/ \   ',
    '  /   *  ',
    ' /|   |\ ',
    '* |   | *',
    ' \|   |/ ',
    '  *   *  ',
    '   \ /   ',
    '    *    ',
  ]], 
  ['input38', [
    '  *   *  ',
    ' / \ /|\ ',
    '*   * | *',
    ' \  | | |',
    '  * | | |',
    ' / \| | |',
    '*   * | *',
    ' \    |/ ',
    '  \   *  ',
    '   \ /   ',
    '    *    ',
  ]], 
  ['input39', [
    '    *    ',
    '   / \   ',
    '  *   *  ',
    ' / \  |\ ',
    '*   \ | *',
    '|\   \| |',
    '| \   * |',
    '|  \  | |',
    '|   \ | |',
    '|    \| |',
    '|     * |',
    '|     | |',
    '*     | *',
    ' \    |/ ',
    '  \   *  ',
    '   \ /   ',
    '    *    ',
  ]], 
  ['input40', [
    '      *    ',
    '     /|    ',
    '    / |    ',
    '   /  |    ',
    '  /   |    ',
    ' /    |    ',
    '*   * |    ',
    ' \  |\|    ',
    '  \ | \    ',
    '   \| |\   ',
    '    \ | \  ',
    '    |\|  \ ',
    '    | *   *',
    '    |    / ',
    '    |   /  ',
    '    |  /   ',
    '    | /    ',
    '    |/     ',
    '    *      ',
  ]], 
  ['input41', [
    '        *  ',
    '       /|  ',
    '  *   * |  ',
    ' / \  |\|  ',
    '*   \ | \  ',
    ' \   \| |\ ',
    '  \   | | *',
    '   \  |\|/ ',
    '    \ | *  ',
    '     \|    ',
    '      \    ',
    '      |\   ',
    '      | *  ',
    '      |/   ',
    '      *    ',
  ]], 
  ['input42', [
    '  *    ',
    '  |\   ',
    '* | \  ',
    '|\|  \ ',
    '| *   *',
    '| |\ / ',
    '| | *  ',
    '| |/ \ ',
    '| *   *',
    '|/|  / ',
    '* | /  ',
    '  |/   ',
    '  *    ',
  ]], 
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

def makePicture(nodes, node2index, edges, edge_precedences_back_to_front, slack):
  print("        in makePicture")
  # If input was this:
  #       *
  #      /|
  #     * |
  #      \|
  #       *
  # slack=1:
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
  # slack=0:
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

  # Syndrome of a node is the bit pattern of which incident edges exist, in this order:
  #    501
  #     @
  #    432
  syndromes = [[False]*6 for node in nodes]
  for inode0,inode1 in edges:
    irow0,icol0 = nodes[inode0]
    irow1,icol1 = nodes[inode1]
    assert irow0 < irow1
    if icol0 < icol1:
      syndromes[inode0][2] = True
      syndromes[inode1][5] = True
    elif icol0 > icol1:
      syndromes[inode0][4] = True
      syndromes[inode1][1] = True
    else:
      syndromes[inode1][0] = True
      syndromes[inode0][3] = True
  def syndrome2string(syndrome): return ''.join('1' if x else '0' for x in syndrome)
  print("          syndromes = %r" % ([syndrome2string(syndrome) for syndrome in syndromes],))

  # For now, handle edge overlaps by topsort.
  # Note that, in general, a topsort may not exist!  But I'm not sure
  # whether there are any of examples of that in the game.

  def topsort(nodes, edges):
    # cbb: cycle failure is by stack overflow
    assert type(nodes) == list
    preds = dict((node,[]) for node in nodes)
    for node0,node1 in edges:
      preds[node1].append(node0)
    answerList = []
    answerSet = set()
    def emitPredsAndSelf(node):
      if node not in answerSet:
        for pred in preds[node]:
          emitPredsAndSelf(pred)
        assert node not in answerSet
        answerList.append(node)
        answerSet.add(node)
    for node in nodes:
    #for node in reversed(nodes):
      emitPredsAndSelf(node)
    return answerList

  if True:
    assert topsort([], []) == []
    assert topsort([0], []) == [0]
    assert topsort([0,1], [(0,1)]) == [0,1]
    assert topsort([0,1], [(1,0)]) == [1,0]
    assert topsort([0,1,2], [(2,1),(0,2)]) == [0,2,1]

  edge_order = topsort(list(set(a for a,b in edge_precedences_back_to_front).union(set(b for a,b in edge_precedences_back_to_front))),
                       edge_precedences_back_to_front)
  print("          edge_order = %r" % (edge_order,))

  edge_order = topsort(list(range(len(edges))), edge_precedences_back_to_front)
  print("          edge_order = %r" % (edge_order,))


  minrow = min(irow for (irow,icol) in nodes)
  maxrow = max(irow for (irow,icol) in nodes)
  mincol = min(icol for (irow,icol) in nodes)
  maxcol = max(icol for (irow,icol) in nodes)
  print("          minrow = %r" % (minrow,))
  print("          maxrow = %r" % (maxrow,))
  print("          mincol = %r" % (mincol,))
  print("          maxcol = %r" % (maxcol,))

  # maxrow-minrow = 0: 9 output rows, 5 output cols
  #     *
  #    / \
  #   *   *
  #   |\ /|
  #   * * *
  #    \|/
  #     *
  # If slack is 0, there 8 more output rows for every additional input row.
  # If slack is 1, there are 9 more. etc.
  assert (maxrow-minrow)%2 == 0
  assert (maxcol-mincol)%2 == 0
  n_rows_out = 7 + (maxrow-minrow)//2 * (6+slack)
  print("          n_rows_out = %r" % (n_rows_out,))
  n_cols_out = 5 + (maxcol-mincol)//2 * (6+slack)
  print("          n_cols_out = %r" % (n_cols_out,))

  answer = [[' ' for icol in range(n_cols_out)] for irow in range(n_rows_out)]



  for iedge in edge_order:
    inode0,inode1  = edges[iedge]
    irow0_in,icol0_in = nodes[inode0]
    irow1_in,icol1_in = nodes[inode1]
    irow0_out = 4 + (irow0_in-minrow)//2 * (6+slack)
    icol0_out = 2 + (icol0_in-mincol)//2 * (6+slack)
    irow1_out = 4 + (irow1_in-minrow)//2 * (6+slack)
    icol1_out = 2 + (icol1_in-mincol)//2 * (6+slack)
    assert irow0_in < irow1_in

    # Note that the exact bounds are empirical.  Too short, and it leaves a gap.  Too long, and it interferes with nodes.
    if icol0_in == icol1_in:
      # vertical
      for irow_out in range(irow0_out + 2, irow1_out+1 - 2):
        answer[irow_out][icol0_out-2] = '|'
        answer[irow_out][icol0_out-1] = ' '
        answer[irow_out][icol0_out] = '|'
        answer[irow_out][icol0_out+1] = ' '
        answer[irow_out][icol0_out+2] = '|'
    elif icol0_in < icol1_in:
      # Pointing SE
      for irow_out in range(irow0_out + 1, irow1_out+1 - 2):
        answer[irow_out+1][icol0_out-1 + (irow_out-irow0_out)] = '\\'
        answer[irow_out+0][icol0_out-1 + (irow_out-irow0_out)] = ' '
        answer[irow_out][icol0_out + (irow_out-irow0_out)] = '\\'
        answer[irow_out-0][icol0_out+1 + (irow_out-irow0_out)] = ' '
        answer[irow_out-1][icol0_out+1 + (irow_out-irow0_out)] = ' '
        answer[irow_out-1][icol0_out+2 + (irow_out-irow0_out)] = ' '
        answer[irow_out-2][icol0_out+2 + (irow_out-irow0_out)] = '\\'
    elif icol0_in > icol1_in:
      # Pointing SW
      for irow_out in range(irow0_out + 1, irow1_out+1 - 2):
        answer[irow_out-2][icol0_out-2 - (irow_out-irow0_out)] = '/'
        answer[irow_out-1][icol0_out-2 - (irow_out-irow0_out)] = ' '
        answer[irow_out-1][icol0_out-1 - (irow_out-irow0_out)] = ' '
        answer[irow_out-0][icol0_out-1 - (irow_out-irow0_out)] = ' '
        answer[irow_out][icol0_out - (irow_out-irow0_out)] = '/'
        answer[irow_out+0][icol0_out+1 - (irow_out-irow0_out)] = ' '
        answer[irow_out+1][icol0_out+1 - (irow_out-irow0_out)] = '/'
    else:
      assert False



  # periods mean transparent
  node_sprite_NE = [
    r'../  ',
    r'./   ',
    r'*   /',
    r'|\ / ',
    r'* * /',
    r'.\|/.',
    r'@.*..',
  ]
  node_sprite_NW = [
    r'  \..',
    r'   \.',
    r'\   *',
    r' \ /|',
    r'\ * *',
    r'.\|/.',
    r'..*.@',
  ]
  node_sprite_S = [
    r'..*..',
    r'./ \.',
    r'* @ *',
    r'|\ /|',
    r'| * |',
    r'| | |',
    r'| | |',
  ]
  node_sprite = [
    r'..*..',
    r'./ \.',
    r'*   *',
    r'|\ /|',
    r'* @ *',
    r'.\|/.',
    r'..*..',
  ]
  node_sprite_N = [
    r'| | |',
    r'| | |',
    r'| | |',
    r'| | |',
    r'* | *',
    r'.\|/.',
    r'..@..',
  ]
  node_sprite_SE = [
    r'..*..',
    r'./ \.',
    r'@   .',
    r'|\  .',
    r'* \ .',
    r'.\ \.',
    r'..\ .',
  ]
  node_sprite_SW = [
    r'..*..',
    r'./ \.',
    r'.   @',
    r'.  /|',
    r'. / *',
    r'./ /.',
    r'. /..',
  ]
  def findTheAtSign(sprite):
    answer = None
    for irow in range(len(sprite)):
      for icol in range(len(sprite[irow])):
        if sprite[irow][icol] == '@':
          assert answer is None
          answer = (irow,icol)
    return answer
  node_sprite_NE_center_row,node_sprite_NE_center_col = findTheAtSign(node_sprite_NE)
  node_sprite_NW_center_row,node_sprite_NW_center_col = findTheAtSign(node_sprite_NW)
  node_sprite_S_center_row,node_sprite_S_center_col = findTheAtSign(node_sprite_S)
  node_sprite_center_row,node_sprite_center_col = findTheAtSign(node_sprite)
  node_sprite_N_center_row,node_sprite_N_center_col = findTheAtSign(node_sprite_N)
  node_sprite_SW_center_row,node_sprite_SW_center_col = findTheAtSign(node_sprite_SW)
  node_sprite_SE_center_row,node_sprite_SE_center_col = findTheAtSign(node_sprite_SE)

  nspriterows = len(node_sprite)
  nspritecols = len(node_sprite[0])
  for inode in range(len(nodes)):
  #for inode in reversed(range(len(nodes))):
    row_in,col_in = nodes[inode]
    node_center_row_out = 4 + (row_in-minrow)//2 * (6+slack)
    node_center_col_out = 2 + (col_in-mincol)//2 * (6+slack)
    answer[node_center_row_out][node_center_col_out] = '*'

    if syndromes[inode][1]:  # NE
      for ispriterow in range(nspriterows):
        for ispritecol in range(nspritecols):
          c = node_sprite_NE[ispriterow][ispritecol]
          if c != '.':
            # xor
            if c in '|\\' and answer[node_center_row_out + (ispriterow - node_sprite_NE_center_row)][node_center_col_out + (ispritecol - node_sprite_NE_center_col)] == c:
              answer[node_center_row_out + (ispriterow - node_sprite_NE_center_row)][node_center_col_out + (ispritecol - node_sprite_NE_center_col)] = ' '
            else:
              answer[node_center_row_out + (ispriterow - node_sprite_NE_center_row)][node_center_col_out + (ispritecol - node_sprite_NE_center_col)] = c

    if syndromes[inode][5]:  # NW
      for ispriterow in range(nspriterows):
        for ispritecol in range(nspritecols):
          c = node_sprite_NW[ispriterow][ispritecol]
          if c != '.':
            # xor
            if c in '/|' and answer[node_center_row_out + (ispriterow - node_sprite_NW_center_row)][node_center_col_out + (ispritecol - node_sprite_NW_center_col)] == c:
              answer[node_center_row_out + (ispriterow - node_sprite_NW_center_row)][node_center_col_out + (ispritecol - node_sprite_NW_center_col)] = ' '
            else:
              answer[node_center_row_out + (ispriterow - node_sprite_NW_center_row)][node_center_col_out + (ispritecol - node_sprite_NW_center_col)] = c

    if syndromes[inode][3]:  # S
      for ispriterow in range(nspriterows):
        for ispritecol in range(nspritecols):
          c = node_sprite_S[ispriterow][ispritecol]
          if c != '.':
            # xor
            if c in '/\\' and answer[node_center_row_out + (ispriterow - node_sprite_S_center_row)][node_center_col_out + (ispritecol - node_sprite_S_center_col)] == c:
              answer[node_center_row_out + (ispriterow - node_sprite_S_center_row)][node_center_col_out + (ispritecol - node_sprite_S_center_col)] = ' '
            else:
              answer[node_center_row_out + (ispriterow - node_sprite_S_center_row)][node_center_col_out + (ispritecol - node_sprite_S_center_col)] = c

    if True:
      for ispriterow in range(nspriterows):
        for ispritecol in range(nspritecols):
          c = node_sprite[ispriterow][ispritecol]
          if c != '.':
            # xor
            if c in '|/\\' and answer[node_center_row_out + (ispriterow - node_sprite_center_row)][node_center_col_out + (ispritecol - node_sprite_center_col)] == c:
              answer[node_center_row_out + (ispriterow - node_sprite_center_row)][node_center_col_out + (ispritecol - node_sprite_center_col)] = ' '
            else:
              answer[node_center_row_out + (ispriterow - node_sprite_center_row)][node_center_col_out + (ispritecol - node_sprite_center_col)] = c

    if syndromes[inode][0]:  # N
      for ispriterow in range(nspriterows):
        for ispritecol in range(nspritecols):
          c = node_sprite_N[ispriterow][ispritecol]
          if c != '.':
            # xor
            if c in '/\\' and answer[node_center_row_out + (ispriterow - node_sprite_N_center_row)][node_center_col_out + (ispritecol - node_sprite_N_center_col)] == c:
              answer[node_center_row_out + (ispriterow - node_sprite_N_center_row)][node_center_col_out + (ispritecol - node_sprite_N_center_col)] = ' '
            else:
              answer[node_center_row_out + (ispriterow - node_sprite_N_center_row)][node_center_col_out + (ispritecol - node_sprite_N_center_col)] = c


    if syndromes[inode][2]:  # SE
      for ispriterow in range(nspriterows):
        print("  ispriterow=%r" % (ispriterow,))
        for ispritecol in range(nspritecols):
          c = node_sprite_SE[ispriterow][ispritecol]
          if c != '.':
            # xor
            if c in '/|' and answer[node_center_row_out + (ispriterow - node_sprite_SE_center_row)][node_center_col_out + (ispritecol - node_sprite_SE_center_col)] == c:
              answer[node_center_row_out + (ispriterow - node_sprite_SE_center_row)][node_center_col_out + (ispritecol - node_sprite_SE_center_col)] = ' '
            else:
              answer[node_center_row_out + (ispriterow - node_sprite_SE_center_row)][node_center_col_out + (ispritecol - node_sprite_SE_center_col)] = c

    if syndromes[inode][4]:  # SW
      for ispriterow in range(nspriterows):
        for ispritecol in range(nspritecols):
          c = node_sprite_SW[ispriterow][ispritecol]
          if c != '.':
            # xor
            if c in '\\|' and answer[node_center_row_out + (ispriterow - node_sprite_SW_center_row)][node_center_col_out + (ispritecol - node_sprite_SW_center_col)] == c:
              answer[node_center_row_out + (ispriterow - node_sprite_SW_center_row)][node_center_col_out + (ispritecol - node_sprite_SW_center_col)] = ' '
            else:
              answer[node_center_row_out + (ispriterow - node_sprite_SW_center_row)][node_center_col_out + (ispritecol - node_sprite_SW_center_col)] = c

  ###############
  #   *         #
  #  / \        #
  # *   *       #
  # |\ /|\      #
  # * * * \     #
  # |\|/|  \    #
  # | * |   *   #
  # | |\|\ / \  #
  # | | | *   * #
  # | | |/|\ /| #
  # | | / * * * #
  # | |/|  \|/  #
  # | * | / *   #
  # |/ \|/ /    #
  # *   * /     #
  # |\ /|/      #
  # * * *       #
  #  \|/        #
  #   *         #
  ###############

  ###############
  #   *         #
  #  / \        #
  # *   *       #
  # |\ /|\      #
  # * * * \     #
  # |\|/|  \    #
  # | * |   *   #
  # | |\|\ / \  #
  # | | | *   * #
  # | | |/|\ /| #
  # | | | * * * #
  # | | |  \|/  #
  # | | | / *   #
  # | | |/ /    #
  # * | * /     #
  # |\|/|/      #
  # * * *       #
  #  \|/        #
  #   *         #
  ###############





  # Question: how do we decide what the picture looks like
  # in the immediate vicinity of a node?
  # Well, it's a function of which of the 6 directions have an incident edge,
  # so there are 64 possibilities.
  # Let's see, the all-edges all-over case looks like this:
  #
  #       *   | | |   *   | | |   *
  #       |\  | | |  /|\  | | |  /|
  #       * \ | | | / * \ | | | / *
  #       |\ \| | |/ /|\ \| | |/ /|
  #       | \ * | * / | \ * | * / |
  #       | |/ \|/ \| | |/ \|/ \| |
  #       | |   *   | | |   *   | |
  #       | |  /|\  | | |  /|\  | |
  #       | | / * \ | | | / * \ | |
  #       | |/ /|\ \| | |/ /|\ \| |
  #       | * / | \ * | * / | \ * |
  #       |/ \| | |/ \|/ \| | |/ \|
  #       *   | | |   *   | | |   *
  #       |\  | | |  /|\  | | |  /|
  #       * \ | | | / * \ | | | / *
  #       |\ \| | |/ /|\ \| | |/ /|
  #       | \ * | * / | \ * | * / |
  #       | |/ \|/ \| | |/ \|/ \| |
  #       | |   *   | | |   *   | |
  #       | |  /|\  | | |  /|\  | |
  #       | | / * \ | | | / * \ | |
  #       | |/ /|\ \| | |/ /|\ \| |
  #       | * / | \ * | * / | \ * |
  #       |/ \| | |/ \|/ \| | |/ \|
  #       *   | | |   *   | | |   *
  # Maybe each node should be responsible for its "voronoi region" in some sense?
  # Let's outline the region we know will be unmolested by others.
  # Maximum part we can draw:
  #       *   | | |   *   | | |   *
  #       |\  | | |  /|\  | | |  /|
  #       * \ | | | / # \ | | | / *
  #       |\ \| | |/ #|# \| | |/ /|
  #       | \ * | # # | # # | * / |
  #       | |/ \|# \| | |/ #|/ \| |
  #       | |   #   | | |   #   | |
  #       | |  /#\  | | |  /#\  | |
  #       | | / # \ | | | / # \ | |
  #       | |/ /|\ \| | |/ /|\ \| |
  #       | * / | \ * | * / | \ * |
  #       |/ \| | #/ \|/ \# | |/ \|
  #       *   | | #   *   # | |   *
  #       |\  | | #  /|\  # | |  /|
  #       * \ | | # / * \ # | | / *
  #       |\ \| | #/ /|\ \# | |/ /|
  #       | \ * | # / | \ # | * / |
  #       | |/ \|/ #| | |# \|/ \| |
  #       | |   *   | | |   *   | |
  #       | |  /|\  | | |  /|\  | |
  #       | | / * \ | | | / * \ | |
  #       | |/ /|\ \| | |/ /|\ \| |
  #       | * / | \ # | # / | \ * |
  #       |/ \| | |/ #|# \| | |/ \|
  #       *   | | |   #   | | |   *
  # Idea: each node draws its up-to-three incident edges that are pointed
  # towards the eye; that should be enough to correct anything that wasn't
  # correct.
  # NO, that doesn't work.  E.g. consider the case when it has 
  # 3 pointed away from the eye, and none towards eye.  Have to draw
  # those correctly!

  # Minimum part we *have* to draw,
  # to fix up edges if edges were indiscriminately drawn first:
  #       *   | | |   *   | | |   *
  #       |\  | | |  /|\  | | |  /|
  #       * \ | | | / # \ | | | / *
  #       |\ \| | |/ ### \| | |/ /|
  #       | \ * | * ##### * | * / |
  #       | |/ \|/ \#####/ \|/ \| |
  #       | |   *  #|###|#  *   | |
  #       | |  /|\ #| # |# /|\  | |
  #       | | / * \#| | |#/ * \ | |
  #       | |/ /|\ #| | |# /|\ \| |
  #       | * / | ##* | *## | \ * |
  #       |/ \| | #/ \|/ \# | |/ \|
  #       *   | | ##  *  ## | |   *
  #       |\  | | ## /|\ ## | |  /|
  #       * \ | | ##/ * \## | | / *
  #       |\ \| | ## /#\ ## | |/ /|
  #       | \ * | ##/###\## | * / |
  #       | |/ \|/ ## | ## \|/ \| |
  #       | |   *   | | |   *   | |
  #       | |  /|\  | | |  /|\  | |
  #       | | / * \ | | | / * \ | |
  #       | |/ /|\ \| | |/ /|\ \| |
  #       | * / | \ * | * / | \ * |
  #       |/ \| | |/ \|/ \| | |/ \|
  #       *   | | |   *   | | |   *
  #
  # But there *is* a voronoi region, right?  It's probably a hexagon??
  # Seems like each node should just be responsible for its voronoi region
  # (pretending slack is 0; draw indiscriminate edges beforehand
  # so there will be no gaps in the final picture.
  # I'm a bit confused about where to draw the line though.
  # Seems like as long as we aren't so long that we impinge on others,
  # there is some leeway in how much we can/should draw.
  # (WHY IS THIS SO HARD? seems like we should be able to define a
  # small region, or a large region, just something that works)
  # Ok I'm going to go with that minimal thing I just came up with.

  #
  # IDEA: can we just draw cubes on cubes, and then erase stuff at the end
  # if it's edges between faces facing the same way?  There are only 3 possible
  # face dirs.
  #
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
  # Jeez this seems hard.
  # Let's just draw a bunch of the 64 sprites by hand, for starters,
  # using the minimal mask I decided on earlier.
  # Oh interesting, if all front arms exist, don't need to draw back ones?
  # Hmm so maybe not too many cases?  Hmm.
  # 
  # All fronts:
  #  1?1?1?:
  #   .|...|.
  #   .| . |.
  #   .| | |.
  #   .| | |.
  #   .* | *.
  #   / \|/ \
  #   .  *  .
  #   . /|\ .
  #   ./ * \.
  #   . /.\ .
  #   ./...\.
  #
  # 2 out of 3 fronts:
  #  011?11:
  #   .\.../.
  #   . \./ .
  #   .  *  .
  #   .     .
  #   .*   *.
  #   /     \
  #   .  *  .
  #   . /|\ .
  #   ./ * \.
  #   . /.\ .
  #   ./...\.
  #
  #  11011?:
  #   .|...|.
  #   .| . |.
  #   .| | |.
  #   .| | |.
  #   .* | *.
  #   / \|  /
  #   .  * *.
  #   . /  |.
  #   ./ * |.
  #   . /. |.
  #   ./...|.
  #  1?1101: mirror image of 11011?
  #
  # 1 out of 3 fronts:
  #  110101:   (and maybe can mask out even more of this? keep in mind we need only what would be messed up by adjacent indiscriminate edges)
  #                \| | |/
  #   .|...|.   of  | | | 
  #   .| . |.       | | | 
  #   .| | |.       | | | 
  #   .| | |.      \| | |/
  #   .* | *.       * | * 
  #   \  |  /      \  @  /
  #   .* | *.       * | * 
  #   .| | |.       | | | 
  #   .| | |.       | | | 
  #   .| . |.       | | | 
  #   .|...|.       | | | 
  #
  #  011101:
  #   .\.../.   of  \   / 
  #   . \./ .        \ /  
  #   .  *  .         *   /
  #   .     .      \     / 
  #   .\   *.       \   * /
  #   \ \   \      \ \   \ 
  #   .* \  .       * @   \
  #   .|  \ .       |  \  
  #   .| * \.       | * \ 
  #   .| .\ .       | |\ \
  #   .|...\.       | | \ \
  #                 | | |\
  #  010111: mirror image of 011101

  #  000000:
  #   . ... .
  #   .  .  .
  #   .  *  .
  #   . / \ .
  #   .*   *.
  #    |\ /| 
  #   .* * *.
  #   . \|/ .
  #   .  *  .
  #   .  .  .
  #   . ... .



  # Idea:
  #    1. draw the back 3 arms, all edges
  #    2. draw the middle cube, all edges
  #    3. draw the front 3 arms, all edges
  #    4. erase edges that are between 2 faces facing same direction






  # Convert from arrays of char to strings
  answer = [''.join(line) for line in answer]

  if True:
    # Show the picture
    print("##" + "#"*n_cols_out  + "##")
    for line in answer:
      print("# %s #" % line)
    print("##" + "#"*n_cols_out  + "##")

  print("        out makePicture")
  return answer

def process(name, input, slack):
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

  def findEdgeEndpoints(input,node2index,irow,icol):
    if input[irow][icol] == '|':
      delta = (1,0)
    elif input[irow][icol] == '/':
      delta = (1,-1)
    elif input[irow][icol] == '\\':
      delta = (1,1)
    else:
      return None,None
    jrow0,jcol0 = irow,icol
    while input[jrow0][jcol0] != '*':
      jrow0 -= delta[0]
      jcol0 -= delta[1]
    jrow1,jcol1 = irow,icol
    while input[jrow1][jcol1] != '*':
      jrow1 += delta[0]
      jcol1 += delta[1]
    return node2index[(jrow0,jcol0)], node2index[(jrow1,jcol1)]

  # Find the edges (pairs of indices into nodes).
  # If this gets an out-of-bounds exception, it means input was bogus.
  edges = set()
  for irow in range(len(input)):
    for icol in range(len(input[irow])):
      inode0,inode1 = findEdgeEndpoints(input,node2index,irow,icol)
      if inode0 is not None:
        edges.add((inode0,inode1))
  edges = sorted(edges)  # convert set to list
  print("      edges = %r" % (edges,))
  edge2index = dict(((edges[i],i) for i in range(len(edges))))
  print("      edge2index = %r" % (edge2index,))

  edge_precedences_back_to_front = set()
  for irow in range(len(input)):
    for icol in range(len(input[irow])):
      if input[irow][icol] == '|':
        deltarow,deltacol = (1,0)
      elif input[irow][icol] == '/':
        deltarow,deltacol = (1,-1)
      elif input[irow][icol] == '\\':
        deltarow,deltacol = (1,1)
      else:
        continue
      for sign in (-1,1):
        if (irow+sign*deltarow >= 0 and irow+sign*deltarow < len(input) and
            icol+sign*deltacol >= 0 and icol+sign*deltacol < len(input[irow+sign*deltarow]) and
            input[irow+sign*deltarow][icol+sign*deltacol] != input[irow][icol] and input[irow+sign*deltarow][icol+sign*deltacol] in '|/\\'):
            # This edge is under the other edge.
            edge0 = edge2index[findEdgeEndpoints(input,node2index,irow,icol)]
            edge1 = edge2index[findEdgeEndpoints(input,node2index,irow+sign*deltarow,icol+sign*deltacol)]
            edge_precedences_back_to_front.add((edge0,edge1))
  edge_precedences_back_to_front = sorted(edge_precedences_back_to_front)  # convert set to list
  print("      edge_precedences_back_to_front = %r" % (edge_precedences_back_to_front,))


  picture = makePicture(nodes, node2index, edges, edge_precedences_back_to_front, slack)

  print("    out process(name="+name+")")

slack = 3  # XXX input
ninputs = len(namesAndInputs)
if len(sys.argv) > 1:
  ninputs = int(sys.argv[1])
for i in range(ninputs):
  name,input = namesAndInputs[i]
  print("  i = %d" % (i,))
  process(name, input, slack)


