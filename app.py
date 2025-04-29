import streamlit as st
from streamlit_option_menu import option_menu
from streamlit_card import card
from streamlit_extras.switch_page_button import switch_page
from streamlit_extras.colored_header import colored_header
from streamlit_extras.add_vertical_space import add_vertical_space
import plotly.graph_objects as go
from typing import Dict, List
import json

# Set page config
st.set_page_config(
    page_title='Digital Product Creator',
    layout='wide',
    initial_sidebar_state='collapsed'
)

# Custom CSS for Flowzy-like design
st.markdown('''
<style>
    /* Modern color scheme */
    :root {
        --primary-color: #4F46E5;
        --secondary-color: #818CF8;
        --background-color: #F9FAFB;
        --text-color: #1F2937;
        --border-color: #E5E7EB;
    }
    
    /* Modern container styling */
    .stApp {
        background-color: var(--background-color);
    }
    
    .stButton>button {
        background-color: var(--primary-color);
        color: white;
        border-radius: 8px;
        padding: 0.5rem 1rem;
        border: none;
        box-shadow: 0 1px 2px rgba(0, 0, 0, 0.05);
    }
    
    /* Card styling */
    .css-1r6slb0 {
        background-color: white;
        border-radius: 12px;
        padding: 1.5rem;
        box-shadow: 0 1px 3px rgba(0, 0, 0, 0.1);
    }
    
    /* Header styling */
    h1, h2, h3 {
        color: var(--text-color);
        font-weight: 600;
    }
    
    /* Input field styling */
    .stTextInput>div>div>input {
        border-radius: 8px;
        border: 1px solid var(--border-color);
    }
    
    /* Metric styling */
    .css-1xarl3l {
        background-color: white;
        border-radius: 12px;
        padding: 1rem;
        box-shadow: 0 1px 3px rgba(0, 0, 0, 0.1);
    }
</style>
''', unsafe_allow_html=True)

class DataDrivenUVZAnalyzer:
    def __init__(self):
        self.data_sources = {
            'marketplace_data': {
                'platforms': ['whop', 'gumroad', 'podia', 'kajabi', 'teachable'],
                'metrics': ['revenue', 'sales_volume', 'customer_retention', 'price_points']
            },
            'search_data': {
                'sources': ['google_trends', 'keyword_planner', 'search_volume', 'cpc_data'],
                'metrics': ['search_volume', 'trend_direction', 'competition_level', 'cost_per_click']
            },
            'social_signals': {
                'platforms': ['twitter', 'linkedin', 'reddit', 'quora', 'facebook_groups'],
                'metrics': ['engagement_rate', 'discussion_volume', 'sentiment_analysis', 'problem_frequency']
            }
        }

    def analyze_market_data(self) -> Dict:
        """Simulated market analysis for demo"""
        return {
            'marketplace_metrics': {'revenue': 15000, 'sales': 150},
            'search_metrics': {'volume': 5000, 'trend': 'up'},
            'social_metrics': {'engagement': 0.08, 'sentiment': 0.75}
        }

def create_ui():
    # Top navigation
    selected = option_menu(
        menu_title=None,
        options=["Dashboard", "UVZ Finder", "Product Creator", "Whop Setup"],
        icons=["house", "search", "tools", "shop"],
        default_index=0,
        orientation="horizontal",
        styles={
            "container": {"padding": "0!important", "background-color": "#fff"},
            "icon": {"color": "#4F46E5", "font-size": "16px"}, 
            "nav-link": {
                "font-size": "16px",
                "text-align": "center",
                "padding": "10px",
                "--hover-color": "#EEF2FF",
            },
            "nav-link-selected": {"background-color": "#EEF2FF", "color": "#4F46E5"},
        }
    )
    
    if selected == "Dashboard":
        show_dashboard()
    elif selected == "UVZ Finder":
        show_uvz_finder()
    elif selected == "Product Creator":
        show_product_creator()
    else:
        show_whop_setup()

    if page == "1. UVZ Analysis":
        show_uvz_analysis_page()
    elif page == "2. Product Creation":
        show_product_creation_page()
    elif page == "3. Whop Setup":
        show_whop_setup_page()

def show_dashboard():
    st.title('Digital Product Creator')
    
    # Quick stats cards
    col1, col2, col3, col4 = st.columns(4)
    with col1:
        card(
            title='UVZs Found',
            text='12 Validated Opportunities',
            image='https://img.icons8.com/clouds/100/search.png'
        )
    with col2:
        card(
            title='Avg Success Rate',
            text='92% Success Rate',
            image='https://img.icons8.com/clouds/100/statistics.png'
        )
    with col3:
        card(
            title='Products Created',
            text='45 Digital Products',
            image='https://img.icons8.com/clouds/100/product.png'
        )
    with col4:
        card(
            title='Revenue Generated',
            text='$156,000+',
            image='https://img.icons8.com/clouds/100/money.png'
        )
    
    # Recent UVZs
    colored_header(
        label='Recent Validated UVZs',
        description='Latest opportunities with 90%+ success probability',
        color_name='blue-70'
    )
    
    col1, col2 = st.columns([2,1])
    with col1:
        st.dataframe(
            {
                'UVZ': [
                    'AI Automation System for E-commerce Owners',
                    'Client Acquisition Framework for Coaches',
                    'Content Repurposing System for Creators'
                ],
                'Success Score': ['9.5/10', '9.2/10', '9.0/10'],
                'Monthly Revenue': ['$25,000', '$18,000', '$15,000'],
                'Growth': ['↑ High', '↑ High', '→ Stable']
            },
            hide_index=True,
            use_container_width=True
        )

def show_uvz_finder():
    st.title('UVZ Finder')
    
    # Modern search interface
    with st.container():
        st.markdown(
            '''
            <div style='background-color: white; padding: 2rem; border-radius: 12px; box-shadow: 0 1px 3px rgba(0,0,0,0.1);'>
                <h3>Find Validated UVZs</h3>
                <p style='color: #6B7280;'>Our AI analyzes 150+ data sources to find guaranteed profitable opportunities</p>
            </div>
            ''',
            unsafe_allow_html=True
        )
    
    add_vertical_space(2)
    
    # Analysis options
    col1, col2 = st.columns([2,1])
    
    with col1:
        # Modern data source selector
        st.markdown('<p style="color: #4B5563; font-weight: 600;">Select Data Sources</p>', unsafe_allow_html=True)
        data_sources = st.multiselect(
            '',
            ["Whop", "Gumroad", "Google Trends", "Reddit", "Twitter", "LinkedIn"],
            default=["Whop", "Google Trends", "Reddit"]
        )

        min_revenue = st.number_input("Minimum Monthly Revenue ($)", 
            min_value=1000, value=10000, step=1000)
        min_search_volume = st.number_input("Minimum Monthly Searches", 
            min_value=100, value=1000, step=100)
        
        if st.button("Start Analysis"):
            with st.spinner("Analyzing market data..."):
                progress_bar = st.progress(0)
                for i in range(100):
                    progress_bar.progress(i + 1)
                
                st.success("Analysis Complete!")
                show_uvz_results()

    with col2:
        st.header("Current Analysis")
        st.metric(label="Data Sources Analyzed", value=len(data_sources))
        st.metric(label="Potential UVZs Found", value="12")
        st.metric(label="Highest Score", value="9.2/10")

def show_uvz_results():
    uvzs = pd.DataFrame({
        'UVZ': [
            'Screen Time Optimization for E-commerce Owners',
            'AI Automation Framework for Service Providers',
            'Client Management System for High-Ticket Coaches'
        ],
        'Score': [9.2, 8.8, 8.5],
        'Monthly Revenue': ['$15,000', '$12,000', '$11,000'],
        'Growth Trend': ['↑ Growing', '↑ Growing', '→ Stable']
    })
    
    st.dataframe(uvzs)
    
    st.subheader("Top UVZ Analysis")
    
    categories = ['Revenue Potential', 'Market Demand', 
                 'Competition Level', 'Growth Trend', 'Implementation Ease']
    values = [9.2, 8.8, 9.0, 8.5, 8.9]
    
    fig = go.Figure(data=go.Scatterpolar(
        r=values,
        theta=categories,
        fill='toself'
    ))
    fig.update_layout(
        polar=dict(
            radialaxis=dict(
                visible=True,
                range=[0, 10]
            )),
        showlegend=False
    )
    st.plotly_chart(fig)

def show_product_creator():
    st.title('Product Creator')
    
    # Modern product creation interface
    with st.container():
        st.markdown(
            '''
            <div style='background-color: white; padding: 2rem; border-radius: 12px; box-shadow: 0 1px 3px rgba(0,0,0,0.1);'>
                <h3>Create Your Digital Product</h3>
                <p style='color: #6B7280;'>AI-powered product creation based on 150+ validated references</p>
            </div>
            ''',
            unsafe_allow_html=True
        )
    
    add_vertical_space(2)
    
    # Product format cards
    col1, col2, col3 = st.columns(3)
    
    with col1:
        digital_course = card(
            title='Digital Course',
            text='Masterclass, Bootcamp, or Coaching Program',
            image='https://img.icons8.com/clouds/100/training.png',
            styles={
                "card": {"background-color": "#EEF2FF"},
                "title": {"color": "#4F46E5"}
            }
        )
    
    with col2:
        done_for_you = card(
            title='Done-for-You',
            text='Service Package or Implementation Package',
            image='https://img.icons8.com/clouds/100/service.png'
        )
    
    with col3:
        templates = card(
            title='Templates/Frameworks',
            text='Playbook, Toolkit, or Swipe File',
            image='https://img.icons8.com/clouds/100/template.png'
        )
    
    # Show format-specific options based on selection
    if digital_course:
        show_course_creator()
    elif done_for_you:
        show_service_creator()
    elif templates:
        show_template_creator()
    
    if format_type == "Digital Course":
        show_course_creator()

def show_course_creator():
    st.subheader("Course Structure")
    
    num_modules = st.number_input("Number of Modules", 1, 20, 5)
    
    for i in range(num_modules):
        st.write(f"### Module {i+1}")
        module_name = st.text_input(f"Module {i+1} Name")
        num_lessons = st.number_input(f"Number of Lessons in Module {i+1}", 1, 10, 3)
        
        for j in range(num_lessons):
            st.write(f"Lesson {j+1}")
            lesson_name = st.text_input(f"Module {i+1} - Lesson {j+1} Name")
            content_type = st.selectbox(
                f"Content Type for Lesson {j+1}",
                ["Video", "Text", "Interactive", "Quiz"],
                key=f"m{i}l{j}"
            )

def show_whop_setup():
    st.title('Whop Setup')
    
    # Modern Whop setup interface
    with st.container():
        st.markdown(
            '''
            <div style='background-color: white; padding: 2rem; border-radius: 12px; box-shadow: 0 1px 3px rgba(0,0,0,0.1);'>
                <h3>Set Up Your Whop Product</h3>
                <p style='color: #6B7280;'>Optimize your product for maximum conversions on Whop</p>
            </div>
            ''',
            unsafe_allow_html=True
        )
    
    add_vertical_space(2)
    
    # Product details in a modern card
    with st.container():
        st.markdown(
            '''
            <div style='background-color: white; padding: 2rem; border-radius: 12px; box-shadow: 0 1px 3px rgba(0,0,0,0.1);'>
                <h4 style='color: #4F46E5; margin-bottom: 1rem;'>Product Details</h4>
            </div>
            ''',
            unsafe_allow_html=True
        )
        
        col1, col2 = st.columns(2)
        with col1:
            title = st.text_input('Product Title', placeholder='Enter a compelling title')
            subtitle = st.text_input('Subtitle', placeholder='Brief, powerful subtitle')
        with col2:
            price = st.number_input('Price ($)', min_value=0, value=997)
            category = st.selectbox('Category', ['Course', 'Template', 'Service'])
    
    add_vertical_space(2)
    
    # Product description
    with st.container():
        st.markdown(
            '''
            <div style='background-color: white; padding: 2rem; border-radius: 12px; box-shadow: 0 1px 3px rgba(0,0,0,0.1);'>
                <h4 style='color: #4F46E5; margin-bottom: 1rem;'>Product Description</h4>
            </div>
            ''',
            unsafe_allow_html=True
        )
        
        description = st.text_area('', placeholder='Enter your product description', height=200)
        
        col1, col2 = st.columns(2)
        with col1:
            features = st.text_area('Key Features (one per line)', height=150)
        with col2:
            benefits = st.text_area('Benefits (one per line)', height=150)
    
    add_vertical_space(2)
    
    # Pricing and packages
    with st.container():
        st.markdown(
            '''
            <div style='background-color: white; padding: 2rem; border-radius: 12px; box-shadow: 0 1px 3px rgba(0,0,0,0.1);'>
                <h4 style='color: #4F46E5; margin-bottom: 1rem;'>Pricing & Packages</h4>
            </div>
            ''',
            unsafe_allow_html=True
        )
        
        pricing_model = st.selectbox('Pricing Model', ['One-time', 'Subscription', 'Tiered'])
        
        if pricing_model == 'Tiered':
            col1, col2, col3 = st.columns(3)
            with col1:
                st.number_input('Basic Tier ($)', min_value=0, value=497)
            with col2:
                st.number_input('Pro Tier ($)', min_value=0, value=997)
            with col3:
                st.number_input('Elite Tier ($)', min_value=0, value=1997)
    
    # Launch button
    st.button('Launch on Whop', use_container_width=True)
    
    if pricing_model == "Tiered":
        st.subheader("Tier Setup")
        num_tiers = st.number_input("Number of Tiers", 1, 5, 3)
        
        for i in range(num_tiers):
            st.write(f"### Tier {i+1}")
            tier_name = st.text_input(f"Tier {i+1} Name")
            tier_price = st.number_input(f"Tier {i+1} Price ($)", 
                min_value=0, value=97)
            tier_features = st.text_area(f"Tier {i+1} Features")

    st.header("Launch Settings")
    launch_date = st.date_input("Launch Date")
    launch_type = st.selectbox(
        "Launch Type",
        ["Immediate", "Pre-launch", "Scheduled"]
    )

if __name__ == "__main__":
    create_ui()
