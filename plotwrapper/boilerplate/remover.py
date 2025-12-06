from matplotlib.axes import Axes 



class BoilerplateRemover:

    @staticmethod
    def reduce_boilerplate(ax: Axes, *args, **kwargs):
        
        #
        # labeling
        #
        if args[0]:
            ax.set_title(args[0])
        if args[1]:
            ax.set_xlabel(args[1])
        if args[2]:
            ax.set_ylabel(args[2])
        
        #
        # ranges
        #
        if args[3]:
            ax.set_xlim(args[3])
        if args[4]:
            ax.set_ylim(args[4])
        
        #
        # legend
        #
        try:
            if kwargs["label"]:
                ax.legend(
                    loc = "upper left", 
                    bbox_to_anchor = (1.0, 1.015),           
                    fontsize=10
                )
        except Exception as e:
            print(e)
            pass       
     
        #
        # grid
        #
        ax.set_axisbelow(True)
        ax.grid(True)
