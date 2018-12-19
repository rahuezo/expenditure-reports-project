def fix_rows(rows): 
    print "\t\nFixing rows"
    for i in xrange(len(rows)):
        print "Current row: ", rows[i]
        if len(rows[i]) > 0 and ("\n" in str(rows[i]) or "\r" in str(rows[i])):
            # Fix first column
            
            if isinstance(rows[i][0], basestring):
                rows[i][0] = rows[i][0].replace("\r", "\n")
                rows[i][0] = rows[i][0].replace("\n", " ")
                rows[i][0] = " ".join(rows[i][0].split())

            # Fix third column
            if isinstance(rows[i][2], basestring):
                rows[i][2] = rows[i][2].replace("\r", "\n")
                rows[i][2] = rows[i][2].replace("\n", " ")
                rows[i][2] = " ".join(rows[i][2].split())
    return rows
