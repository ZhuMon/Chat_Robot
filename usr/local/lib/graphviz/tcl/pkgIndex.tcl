package ifneeded Tcldot 2.38.0 "
	load [file join $dir libtcldot.0.dylib] Tcldot"
package ifneeded Tclpathplan 2.38.0 "
	load [file join $dir libtclplan.0.dylib] Tclpathplan"
package ifneeded Tkspline 2.38.0 "
	package require Tk 8.3
	load [file join $dir libtkspline.0.dylib] Tkspline"
# end
