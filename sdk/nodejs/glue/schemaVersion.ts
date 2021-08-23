// *** WARNING: this file was generated by pulumigen. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

import * as pulumi from "@pulumi/pulumi";
import { input as inputs, output as outputs } from "../types";
import * as utilities from "../utilities";

/**
 * http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-glue-schemaversion.html
 */
export class SchemaVersion extends pulumi.CustomResource {
    /**
     * Get an existing SchemaVersion resource's state with the given name, ID, and optional extra
     * properties used to qualify the lookup.
     *
     * @param name The _unique_ name of the resulting resource.
     * @param id The _unique_ provider ID of the resource to lookup.
     * @param opts Optional settings to control the behavior of the CustomResource.
     */
    public static get(name: string, id: pulumi.Input<pulumi.ID>, opts?: pulumi.CustomResourceOptions): SchemaVersion {
        return new SchemaVersion(name, undefined as any, { ...opts, id: id });
    }

    /** @internal */
    public static readonly __pulumiType = 'aws-native:glue:SchemaVersion';

    /**
     * Returns true if the given object is an instance of SchemaVersion.  This is designed to work even
     * when multiple copies of the Pulumi SDK have been loaded into the same process.
     */
    public static isInstance(obj: any): obj is SchemaVersion {
        if (obj === undefined || obj === null) {
            return false;
        }
        return obj['__pulumiType'] === SchemaVersion.__pulumiType;
    }

    /**
     * http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-glue-schemaversion.html#cfn-glue-schemaversion-schema
     */
    public readonly schema!: pulumi.Output<outputs.glue.SchemaVersionSchema>;
    /**
     * http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-glue-schemaversion.html#cfn-glue-schemaversion-schemadefinition
     */
    public readonly schemaDefinition!: pulumi.Output<string>;
    public /*out*/ readonly versionId!: pulumi.Output<string>;

    /**
     * Create a SchemaVersion resource with the given unique name, arguments, and options.
     *
     * @param name The _unique_ name of the resource.
     * @param args The arguments to use to populate this resource's properties.
     * @param opts A bag of options that control this resource's behavior.
     */
    constructor(name: string, args: SchemaVersionArgs, opts?: pulumi.CustomResourceOptions) {
        let inputs: pulumi.Inputs = {};
        opts = opts || {};
        if (!opts.id) {
            if ((!args || args.schema === undefined) && !opts.urn) {
                throw new Error("Missing required property 'schema'");
            }
            if ((!args || args.schemaDefinition === undefined) && !opts.urn) {
                throw new Error("Missing required property 'schemaDefinition'");
            }
            inputs["schema"] = args ? args.schema : undefined;
            inputs["schemaDefinition"] = args ? args.schemaDefinition : undefined;
            inputs["versionId"] = undefined /*out*/;
        } else {
            inputs["schema"] = undefined /*out*/;
            inputs["schemaDefinition"] = undefined /*out*/;
            inputs["versionId"] = undefined /*out*/;
        }
        if (!opts.version) {
            opts = pulumi.mergeOptions(opts, { version: utilities.getVersion()});
        }
        super(SchemaVersion.__pulumiType, name, inputs, opts);
    }
}

/**
 * The set of arguments for constructing a SchemaVersion resource.
 */
export interface SchemaVersionArgs {
    /**
     * http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-glue-schemaversion.html#cfn-glue-schemaversion-schema
     */
    schema: pulumi.Input<inputs.glue.SchemaVersionSchemaArgs>;
    /**
     * http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-glue-schemaversion.html#cfn-glue-schemaversion-schemadefinition
     */
    schemaDefinition: pulumi.Input<string>;
}
