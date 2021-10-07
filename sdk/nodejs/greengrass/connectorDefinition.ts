// *** WARNING: this file was generated by the Pulumi SDK Generator. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

import * as pulumi from "@pulumi/pulumi";
import { input as inputs, output as outputs, enums } from "../types";
import * as utilities from "../utilities";

/**
 * Resource Type definition for AWS::Greengrass::ConnectorDefinition
 *
 * @deprecated ConnectorDefinition is not yet supported by AWS Native, so its creation will currently fail. Please use the classic AWS provider, if possible.
 */
export class ConnectorDefinition extends pulumi.CustomResource {
    /**
     * Get an existing ConnectorDefinition resource's state with the given name, ID, and optional extra
     * properties used to qualify the lookup.
     *
     * @param name The _unique_ name of the resulting resource.
     * @param id The _unique_ provider ID of the resource to lookup.
     * @param opts Optional settings to control the behavior of the CustomResource.
     */
    public static get(name: string, id: pulumi.Input<pulumi.ID>, opts?: pulumi.CustomResourceOptions): ConnectorDefinition {
        pulumi.log.warn("ConnectorDefinition is deprecated: ConnectorDefinition is not yet supported by AWS Native, so its creation will currently fail. Please use the classic AWS provider, if possible.")
        return new ConnectorDefinition(name, undefined as any, { ...opts, id: id });
    }

    /** @internal */
    public static readonly __pulumiType = 'aws-native:greengrass:ConnectorDefinition';

    /**
     * Returns true if the given object is an instance of ConnectorDefinition.  This is designed to work even
     * when multiple copies of the Pulumi SDK have been loaded into the same process.
     */
    public static isInstance(obj: any): obj is ConnectorDefinition {
        if (obj === undefined || obj === null) {
            return false;
        }
        return obj['__pulumiType'] === ConnectorDefinition.__pulumiType;
    }

    public /*out*/ readonly arn!: pulumi.Output<string>;
    public readonly initialVersion!: pulumi.Output<outputs.greengrass.ConnectorDefinitionVersion | undefined>;
    public /*out*/ readonly latestVersionArn!: pulumi.Output<string>;
    public readonly name!: pulumi.Output<string>;
    public readonly tags!: pulumi.Output<any | undefined>;

    /**
     * Create a ConnectorDefinition resource with the given unique name, arguments, and options.
     *
     * @param name The _unique_ name of the resource.
     * @param args The arguments to use to populate this resource's properties.
     * @param opts A bag of options that control this resource's behavior.
     */
    /** @deprecated ConnectorDefinition is not yet supported by AWS Native, so its creation will currently fail. Please use the classic AWS provider, if possible. */
    constructor(name: string, args: ConnectorDefinitionArgs, opts?: pulumi.CustomResourceOptions) {
        pulumi.log.warn("ConnectorDefinition is deprecated: ConnectorDefinition is not yet supported by AWS Native, so its creation will currently fail. Please use the classic AWS provider, if possible.")
        let inputs: pulumi.Inputs = {};
        opts = opts || {};
        if (!opts.id) {
            if ((!args || args.name === undefined) && !opts.urn) {
                throw new Error("Missing required property 'name'");
            }
            inputs["initialVersion"] = args ? args.initialVersion : undefined;
            inputs["name"] = args ? args.name : undefined;
            inputs["tags"] = args ? args.tags : undefined;
            inputs["arn"] = undefined /*out*/;
            inputs["latestVersionArn"] = undefined /*out*/;
        } else {
            inputs["arn"] = undefined /*out*/;
            inputs["initialVersion"] = undefined /*out*/;
            inputs["latestVersionArn"] = undefined /*out*/;
            inputs["name"] = undefined /*out*/;
            inputs["tags"] = undefined /*out*/;
        }
        if (!opts.version) {
            opts = pulumi.mergeOptions(opts, { version: utilities.getVersion()});
        }
        super(ConnectorDefinition.__pulumiType, name, inputs, opts);
    }
}

/**
 * The set of arguments for constructing a ConnectorDefinition resource.
 */
export interface ConnectorDefinitionArgs {
    initialVersion?: pulumi.Input<inputs.greengrass.ConnectorDefinitionVersionArgs>;
    name: pulumi.Input<string>;
    tags?: any;
}
