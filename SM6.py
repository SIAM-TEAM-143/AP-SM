import platform

if platform.architecture()[0] != "64bit":
    print("32bit Not Supported!")
else:
    try:
        import smup6

        # Start the module's main entry point
        if hasattr(smup6, "main_menu"):
            smup6.main_menu()
        elif hasattr(smup6, "main"):
            smup6.main()
        else:
            print("Error:  function.")

    except Exception as e:
        import traceback
        print(f"\nCRITICAL ERROR: {e}")
        traceback.print_exc()
        input("\nPress Enter to exit...")
