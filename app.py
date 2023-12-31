# Core python libraries
from os import getenv
from dotenv import load_dotenv
load_dotenv()

# Third party
from shimoku_api_python import Client

# Local imports
from layout.layout import plot_dashboard

def setup_dashboard(shimoku: Client):
    """
    Setups the navigation of the dashboard
    """
    # Sets the business for the whole module
    shimoku.dashboard.set_business(shimoku.app.business_id)

    # Set the created dashboard, to be page's one
    dashboard_name = 'Platforms Dashboard'
    shimoku.plt.set_dashboard(dashboard_name=dashboard_name)

if __name__ == "__main__":

    # Create the client
    shimoku = Client(
        universe_id=getenv('UNIVERSE_ID'),
        access_token=getenv('API_TOKEN'),
        business_id=getenv('BUSINESS_ID'),
        verbosity='INFO',
        async_execution=True,
    )

    #delete previous dashboard
    shimoku.app.delete_all_business_apps()
    shimoku.dashboard.delete_all_business_dashboards()

    #Setting and plot
    setup_dashboard(shimoku)
    plot_dashboard(shimoku)

    # Execute all plots in asynchronous mode
    shimoku.activate_async_execution()
    shimoku.run()

