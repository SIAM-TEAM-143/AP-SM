import platform

if platform.architecture()[0] != "64bit":
    print("32bit Not Supported!")
else:
    try:
        import CT

        # Start the module's main entry point
        if hasattr(CT, "main_menu"):
            CT.main_menu()
        elif hasattr(CT, "main"):
            CT.main()
        else:
            print("Error:  function.")

    except Exception as e:
        import traceback
        print(f"\nCRITICAL ERROR: {e}")
        traceback.print_exc()
        input("\nPress Enter to exit...")
