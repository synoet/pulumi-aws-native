// *** WARNING: this file was generated by the Pulumi SDK Generator. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

import * as pulumi from "@pulumi/pulumi";
import * as inputs from "../types/input";
import * as outputs from "../types/output";
import * as enums from "../types/enums";
import * as utilities from "../utilities";

/**
 * Represents a table that can be queried within a collaboration
 */
export class ConfiguredTableAssociation extends pulumi.CustomResource {
    /**
     * Get an existing ConfiguredTableAssociation resource's state with the given name, ID, and optional extra
     * properties used to qualify the lookup.
     *
     * @param name The _unique_ name of the resulting resource.
     * @param id The _unique_ provider ID of the resource to lookup.
     * @param opts Optional settings to control the behavior of the CustomResource.
     */
    public static get(name: string, id: pulumi.Input<pulumi.ID>, opts?: pulumi.CustomResourceOptions): ConfiguredTableAssociation {
        return new ConfiguredTableAssociation(name, undefined as any, { ...opts, id: id });
    }

    /** @internal */
    public static readonly __pulumiType = 'aws-native:cleanrooms:ConfiguredTableAssociation';

    /**
     * Returns true if the given object is an instance of ConfiguredTableAssociation.  This is designed to work even
     * when multiple copies of the Pulumi SDK have been loaded into the same process.
     */
    public static isInstance(obj: any): obj is ConfiguredTableAssociation {
        if (obj === undefined || obj === null) {
            return false;
        }
        return obj['__pulumiType'] === ConfiguredTableAssociation.__pulumiType;
    }

    public /*out*/ readonly arn!: pulumi.Output<string>;
    public /*out*/ readonly configuredTableAssociationIdentifier!: pulumi.Output<string>;
    public readonly configuredTableIdentifier!: pulumi.Output<string>;
    public readonly description!: pulumi.Output<string | undefined>;
    public readonly membershipIdentifier!: pulumi.Output<string>;
    public readonly name!: pulumi.Output<string>;
    public readonly roleArn!: pulumi.Output<string>;
    /**
     * An arbitrary set of tags (key-value pairs) for this cleanrooms collaboration.
     */
    public readonly tags!: pulumi.Output<outputs.cleanrooms.ConfiguredTableAssociationTag[] | undefined>;

    /**
     * Create a ConfiguredTableAssociation resource with the given unique name, arguments, and options.
     *
     * @param name The _unique_ name of the resource.
     * @param args The arguments to use to populate this resource's properties.
     * @param opts A bag of options that control this resource's behavior.
     */
    constructor(name: string, args: ConfiguredTableAssociationArgs, opts?: pulumi.CustomResourceOptions) {
        let resourceInputs: pulumi.Inputs = {};
        opts = opts || {};
        if (!opts.id) {
            if ((!args || args.configuredTableIdentifier === undefined) && !opts.urn) {
                throw new Error("Missing required property 'configuredTableIdentifier'");
            }
            if ((!args || args.membershipIdentifier === undefined) && !opts.urn) {
                throw new Error("Missing required property 'membershipIdentifier'");
            }
            if ((!args || args.roleArn === undefined) && !opts.urn) {
                throw new Error("Missing required property 'roleArn'");
            }
            resourceInputs["configuredTableIdentifier"] = args ? args.configuredTableIdentifier : undefined;
            resourceInputs["description"] = args ? args.description : undefined;
            resourceInputs["membershipIdentifier"] = args ? args.membershipIdentifier : undefined;
            resourceInputs["name"] = args ? args.name : undefined;
            resourceInputs["roleArn"] = args ? args.roleArn : undefined;
            resourceInputs["tags"] = args ? args.tags : undefined;
            resourceInputs["arn"] = undefined /*out*/;
            resourceInputs["configuredTableAssociationIdentifier"] = undefined /*out*/;
        } else {
            resourceInputs["arn"] = undefined /*out*/;
            resourceInputs["configuredTableAssociationIdentifier"] = undefined /*out*/;
            resourceInputs["configuredTableIdentifier"] = undefined /*out*/;
            resourceInputs["description"] = undefined /*out*/;
            resourceInputs["membershipIdentifier"] = undefined /*out*/;
            resourceInputs["name"] = undefined /*out*/;
            resourceInputs["roleArn"] = undefined /*out*/;
            resourceInputs["tags"] = undefined /*out*/;
        }
        opts = pulumi.mergeOptions(utilities.resourceOptsDefaults(), opts);
        const replaceOnChanges = { replaceOnChanges: ["configuredTableIdentifier", "membershipIdentifier", "name"] };
        opts = pulumi.mergeOptions(opts, replaceOnChanges);
        super(ConfiguredTableAssociation.__pulumiType, name, resourceInputs, opts);
    }
}

/**
 * The set of arguments for constructing a ConfiguredTableAssociation resource.
 */
export interface ConfiguredTableAssociationArgs {
    configuredTableIdentifier: pulumi.Input<string>;
    description?: pulumi.Input<string>;
    membershipIdentifier: pulumi.Input<string>;
    name?: pulumi.Input<string>;
    roleArn: pulumi.Input<string>;
    /**
     * An arbitrary set of tags (key-value pairs) for this cleanrooms collaboration.
     */
    tags?: pulumi.Input<pulumi.Input<inputs.cleanrooms.ConfiguredTableAssociationTagArgs>[]>;
}
