// *** WARNING: this file was generated by the Pulumi SDK Generator. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

import * as pulumi from "@pulumi/pulumi";
import * as inputs from "../types/input";
import * as outputs from "../types/output";
import * as enums from "../types/enums";
import * as utilities from "../utilities";

/**
 * Resource Type definition for AWS::OpsWorks::App
 *
 * @deprecated App is not yet supported by AWS Native, so its creation will currently fail. Please use the classic AWS provider, if possible.
 */
export class App extends pulumi.CustomResource {
    /**
     * Get an existing App resource's state with the given name, ID, and optional extra
     * properties used to qualify the lookup.
     *
     * @param name The _unique_ name of the resulting resource.
     * @param id The _unique_ provider ID of the resource to lookup.
     * @param opts Optional settings to control the behavior of the CustomResource.
     */
    public static get(name: string, id: pulumi.Input<pulumi.ID>, opts?: pulumi.CustomResourceOptions): App {
        pulumi.log.warn("App is deprecated: App is not yet supported by AWS Native, so its creation will currently fail. Please use the classic AWS provider, if possible.")
        return new App(name, undefined as any, { ...opts, id: id });
    }

    /** @internal */
    public static readonly __pulumiType = 'aws-native:opsworks:App';

    /**
     * Returns true if the given object is an instance of App.  This is designed to work even
     * when multiple copies of the Pulumi SDK have been loaded into the same process.
     */
    public static isInstance(obj: any): obj is App {
        if (obj === undefined || obj === null) {
            return false;
        }
        return obj['__pulumiType'] === App.__pulumiType;
    }

    public readonly appSource!: pulumi.Output<outputs.opsworks.AppSource | undefined>;
    public readonly attributes!: pulumi.Output<any | undefined>;
    public readonly dataSources!: pulumi.Output<outputs.opsworks.AppDataSource[] | undefined>;
    public readonly description!: pulumi.Output<string | undefined>;
    public readonly domains!: pulumi.Output<string[] | undefined>;
    public readonly enableSsl!: pulumi.Output<boolean | undefined>;
    public readonly environment!: pulumi.Output<outputs.opsworks.AppEnvironmentVariable[] | undefined>;
    public readonly name!: pulumi.Output<string>;
    public readonly shortname!: pulumi.Output<string | undefined>;
    public readonly sslConfiguration!: pulumi.Output<outputs.opsworks.AppSslConfiguration | undefined>;
    public readonly stackId!: pulumi.Output<string>;
    public readonly type!: pulumi.Output<string>;

    /**
     * Create a App resource with the given unique name, arguments, and options.
     *
     * @param name The _unique_ name of the resource.
     * @param args The arguments to use to populate this resource's properties.
     * @param opts A bag of options that control this resource's behavior.
     */
    /** @deprecated App is not yet supported by AWS Native, so its creation will currently fail. Please use the classic AWS provider, if possible. */
    constructor(name: string, args: AppArgs, opts?: pulumi.CustomResourceOptions) {
        pulumi.log.warn("App is deprecated: App is not yet supported by AWS Native, so its creation will currently fail. Please use the classic AWS provider, if possible.")
        let resourceInputs: pulumi.Inputs = {};
        opts = opts || {};
        if (!opts.id) {
            if ((!args || args.stackId === undefined) && !opts.urn) {
                throw new Error("Missing required property 'stackId'");
            }
            if ((!args || args.type === undefined) && !opts.urn) {
                throw new Error("Missing required property 'type'");
            }
            resourceInputs["appSource"] = args ? args.appSource : undefined;
            resourceInputs["attributes"] = args ? args.attributes : undefined;
            resourceInputs["dataSources"] = args ? args.dataSources : undefined;
            resourceInputs["description"] = args ? args.description : undefined;
            resourceInputs["domains"] = args ? args.domains : undefined;
            resourceInputs["enableSsl"] = args ? args.enableSsl : undefined;
            resourceInputs["environment"] = args ? args.environment : undefined;
            resourceInputs["name"] = args ? args.name : undefined;
            resourceInputs["shortname"] = args ? args.shortname : undefined;
            resourceInputs["sslConfiguration"] = args ? args.sslConfiguration : undefined;
            resourceInputs["stackId"] = args ? args.stackId : undefined;
            resourceInputs["type"] = args ? args.type : undefined;
        } else {
            resourceInputs["appSource"] = undefined /*out*/;
            resourceInputs["attributes"] = undefined /*out*/;
            resourceInputs["dataSources"] = undefined /*out*/;
            resourceInputs["description"] = undefined /*out*/;
            resourceInputs["domains"] = undefined /*out*/;
            resourceInputs["enableSsl"] = undefined /*out*/;
            resourceInputs["environment"] = undefined /*out*/;
            resourceInputs["name"] = undefined /*out*/;
            resourceInputs["shortname"] = undefined /*out*/;
            resourceInputs["sslConfiguration"] = undefined /*out*/;
            resourceInputs["stackId"] = undefined /*out*/;
            resourceInputs["type"] = undefined /*out*/;
        }
        opts = pulumi.mergeOptions(utilities.resourceOptsDefaults(), opts);
        super(App.__pulumiType, name, resourceInputs, opts);
    }
}

/**
 * The set of arguments for constructing a App resource.
 */
export interface AppArgs {
    appSource?: pulumi.Input<inputs.opsworks.AppSourceArgs>;
    attributes?: any;
    dataSources?: pulumi.Input<pulumi.Input<inputs.opsworks.AppDataSourceArgs>[]>;
    description?: pulumi.Input<string>;
    domains?: pulumi.Input<pulumi.Input<string>[]>;
    enableSsl?: pulumi.Input<boolean>;
    environment?: pulumi.Input<pulumi.Input<inputs.opsworks.AppEnvironmentVariableArgs>[]>;
    name?: pulumi.Input<string>;
    shortname?: pulumi.Input<string>;
    sslConfiguration?: pulumi.Input<inputs.opsworks.AppSslConfigurationArgs>;
    stackId: pulumi.Input<string>;
    type: pulumi.Input<string>;
}
