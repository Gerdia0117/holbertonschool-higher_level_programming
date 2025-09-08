#!/usr/bin/python3.10

if __name__ == "__main__":
    import sys
    import importlib.util
    
    # Add /tmp to sys.path
    sys.path.insert(0, '/tmp')
    
    try:
        import hidden_4
        names = dir(hidden_4)
        for name in sorted(names):
            if not name.startswith("__"):
                print(name)
    except ImportError as e:
        # Try alternative method if direct import fails
        spec = importlib.util.spec_from_file_location("hidden_4", "/tmp/hidden_4.pyc")
        if spec and spec.loader:
            hidden_4 = importlib.util.module_from_spec(spec)
            spec.loader.exec_module(hidden_4)
            names = dir(hidden_4)
            for name in sorted(names):
                if not name.startswith("__"):
                    print(name)
