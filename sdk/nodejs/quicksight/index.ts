// *** WARNING: this file was generated by pulumigen. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

import * as pulumi from "@pulumi/pulumi";
import * as utilities from "../utilities";

// Export members:
export * from "./analysis";
export * from "./dashboard";
export * from "./dataSet";
export * from "./dataSource";
export * from "./template";
export * from "./theme";

// Import resources to register:
import { Analysis } from "./analysis";
import { Dashboard } from "./dashboard";
import { DataSet } from "./dataSet";
import { DataSource } from "./dataSource";
import { Template } from "./template";
import { Theme } from "./theme";

const _module = {
    version: utilities.getVersion(),
    construct: (name: string, type: string, urn: string): pulumi.Resource => {
        switch (type) {
            case "aws-native:quicksight:Analysis":
                return new Analysis(name, <any>undefined, { urn })
            case "aws-native:quicksight:Dashboard":
                return new Dashboard(name, <any>undefined, { urn })
            case "aws-native:quicksight:DataSet":
                return new DataSet(name, <any>undefined, { urn })
            case "aws-native:quicksight:DataSource":
                return new DataSource(name, <any>undefined, { urn })
            case "aws-native:quicksight:Template":
                return new Template(name, <any>undefined, { urn })
            case "aws-native:quicksight:Theme":
                return new Theme(name, <any>undefined, { urn })
            default:
                throw new Error(`unknown resource type ${type}`);
        }
    },
};
pulumi.runtime.registerResourceModule("aws-native", "quicksight", _module)
