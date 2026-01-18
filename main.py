"""
main.py
Entry point for the Disneyland Review Analyser project (compatível com tui.py/process.py/visual.py fornecidos).
"""

import sys
import tui
import process
import visual

DATASET_FILE = "Disneyland_reviews.csv"


def run_view_data_menu(reviews: list[dict]) -> None:
    tui.display_view_data_menu()
    choice = tui.get_menu_choice()

    if choice == "A":
        tui.confirm_choice("A", "Most reviewed Parks")
        result = process.most_reviewed_parks(reviews)
        tui.display_most_reviewed_parks(result)

    elif choice == "B":
        tui.confirm_choice("B", "Park Ranking by Nationality")
        loc = tui.get_text_input("Enter nationality / location (e.g., UK): ")
        result = process.park_ranking_by_nationality(reviews, loc)
        tui.display_park_ranking_by_nationality(loc, result)

    elif choice == "C":
        tui.confirm_choice("C", "Most Popular Month by Park")
        park = tui.get_text_input("Enter park name (e.g., Disneyland Paris): ")
        result = process.most_popular_month_by_park(reviews, park)
        tui.display_most_popular_month_by_park(park, result)

    else:
        tui.invalid_option()


def run_visualise_menu(reviews: list[dict]) -> None:
    tui.display_visualise_menu()
    choice = tui.get_menu_choice()

    if choice == "A":
        tui.confirm_choice("A", "Pie chart - number of reviews by park")
        visual.plot_reviews_by_park_pie(reviews)

    elif choice == "B":
        tui.confirm_choice("B", "Top 10 locations by average rating (for a park)")
        park = tui.get_text_input("Enter park name (e.g., Disneyland Paris): ")
        visual.plot_top10_locations_avg_rating(reviews, park)

    elif choice == "C":
        tui.confirm_choice("C", "Average rating by month (for a park)")
        park = tui.get_text_input("Enter park name (e.g., Disneyland Paris): ")
        visual.plot_avg_rating_by_month(reviews, park)

    else:
        tui.invalid_option()


def main() -> None:
    tui.display_title("Disneyland Review Analyser")

    try:
        reviews = process.load_reviews(DATASET_FILE)
    except FileNotFoundError:
        tui.show_message(f"ERROR: Dataset file not found: {DATASET_FILE}")
        sys.exit(1)
    except Exception as exc:
        tui.show_message(f"ERROR: Failed to load dataset: {exc}")
        sys.exit(1)

    tui.show_message("Dataset loaded successfully!")
    tui.show_message(f"Number of rows: {len(reviews)}")

    while True:
        tui.display_main_menu()
        choice = tui.get_menu_choice()

        if choice == "A":
            tui.confirm_choice("A", "View Data")
            run_view_data_menu(reviews)

        elif choice == "B":
            tui.confirm_choice("B", "Visualise Data")
            run_visualise_menu(reviews)

        elif choice == "X":
            tui.confirm_choice("X", "Exit")
            tui.show_message("Bye!")
            break

        else:
            tui.invalid_option()


if __name__ == "__main__":
    main()