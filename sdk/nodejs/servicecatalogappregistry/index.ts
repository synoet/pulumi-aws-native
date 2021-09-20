// *** WARNING: this file was generated by pulumigen. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

import * as pulumi from "@pulumi/pulumi";
import * as utilities from "../utilities";

// Export members:
export * from "./application";
export * from "./attributeGroup";
export * from "./attributeGroupAssociation";
export * from "./resourceAssociation";

// Export enums:
export * from "../types/enums/servicecatalogappregistry";

// Import resources to register:
import { Application } from "./application";
import { AttributeGroup } from "./attributeGroup";
import { AttributeGroupAssociation } from "./attributeGroupAssociation";
import { ResourceAssociation } from "./resourceAssociation";

const _module = {
    version: utilities.getVersion(),
    construct: (name: string, type: string, urn: string): pulumi.Resource => {
        switch (type) {
            case "aws-native:servicecatalogappregistry:Application":
                return new Application(name, <any>undefined, { urn })
            case "aws-native:servicecatalogappregistry:AttributeGroup":
                return new AttributeGroup(name, <any>undefined, { urn })
            case "aws-native:servicecatalogappregistry:AttributeGroupAssociation":
                return new AttributeGroupAssociation(name, <any>undefined, { urn })
            case "aws-native:servicecatalogappregistry:ResourceAssociation":
                return new ResourceAssociation(name, <any>undefined, { urn })
            default:
                throw new Error(`unknown resource type ${type}`);
        }
    },
};
pulumi.runtime.registerResourceModule("aws-native", "servicecatalogappregistry", _module)
