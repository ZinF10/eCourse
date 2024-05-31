from flask_restx import Api as Api_


class Api(Api_):
    def add_namespace(self, ns, path=None):
        if ns not in self.namespaces:
            self.namespaces.append(ns)

            self.sort_namespace()

            if self not in ns.apis:
                ns.apis.append(self)
            if path is not None:
                self.ns_paths[ns] = path

        for r in ns.resources:
            urls = self.ns_urls(ns, r.urls)
            self.register_resource(ns, r.resource, *urls, **r.kwargs)

        for name, definition in ns.models.items():
            self.models[name] = definition
        if not self.blueprint and self.app is not None:
            self._configure_namespace_logger(self.app, ns)

    def sort_namespace(self):
        self.namespaces = sorted(self.namespaces, key=lambda ns: ns.name)
