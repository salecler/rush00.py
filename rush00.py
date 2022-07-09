# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    rush00.py                                          :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: psegura- <psegura-@student.42.fr>          +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2022/07/09 12:48:25 by psegura-          #+#    #+#              #
#    Updated: 2022/07/09 13:13:23 by psegura-         ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

import sys

i = 0

print 'Number of arguments:', len(sys.argv), 'arguments.'

while i < len(sys.argv):
    print 'Argument:', str(sys.argv[i])
    i += 1
