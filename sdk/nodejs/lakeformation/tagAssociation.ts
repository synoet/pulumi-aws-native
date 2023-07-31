// *** WARNING: this file was generated by the Pulumi SDK Generator. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

import * as pulumi from "@pulumi/pulumi";
import * as inputs from "../types/input";
import * as outputs from "../types/output";
import * as enums from "../types/enums";
import * as utilities from "../utilities";

/**
 * A resource schema representing a Lake Formation Tag Association. While tag associations are not explicit Lake Formation resources, this CloudFormation resource can be used to associate tags with Lake Formation entities.
 */
export class TagAssociation extends pulumi.CustomResource {
    /**
     * Get an existing TagAssociation resource's state with the given name, ID, and optional extra
     * properties used to qualify the lookup.
     *
     * @param name The _unique_ name of the resulting resource.
     * @param id The _unique_ provider ID of the resource to lookup.
     * @param opts Optional settings to control the behavior of the CustomResource.
     */
    public static get(name: string, id: pulumi.Input<pulumi.ID>, opts?: pulumi.CustomResourceOptions): TagAssociation {
        return new TagAssociation(name, undefined as any, { ...opts, id: id });
    }

    /** @internal */
    public static readonly __pulumiType = 'aws-native:lakeformation:TagAssociation';

    /**
     * Returns true if the given object is an instance of TagAssociation.  This is designed to work even
     * when multiple copies of the Pulumi SDK have been loaded into the same process.
     */
    public static isInstance(obj: any): obj is TagAssociation {
        if (obj === undefined || obj === null) {
            return false;
        }
        return obj['__pulumiType'] === TagAssociation.__pulumiType;
    }

    /**
     * List of Lake Formation Tags to associate with the Lake Formation Resource
     */
    public readonly lfTags!: pulumi.Output<outputs.lakeformation.TagAssociationLFTagPair[]>;
    /**
     * Resource to tag with the Lake Formation Tags
     */
    public readonly resource!: pulumi.Output<outputs.lakeformation.TagAssociationResource>;
    /**
     * Unique string identifying the resource. Used as primary identifier, which ideally should be a string
     */
    public /*out*/ readonly resourceIdentifier!: pulumi.Output<string>;
    /**
     * Unique string identifying the resource's tags. Used as primary identifier, which ideally should be a string
     */
    public /*out*/ readonly tagsIdentifier!: pulumi.Output<string>;

    /**
     * Create a TagAssociation resource with the given unique name, arguments, and options.
     *
     * @param name The _unique_ name of the resource.
     * @param args The arguments to use to populate this resource's properties.
     * @param opts A bag of options that control this resource's behavior.
     */
    constructor(name: string, args: TagAssociationArgs, opts?: pulumi.CustomResourceOptions) {
        let resourceInputs: pulumi.Inputs = {};
        opts = opts || {};
        if (!opts.id) {
            if ((!args || args.lfTags === undefined) && !opts.urn) {
                throw new Error("Missing required property 'lfTags'");
            }
            if ((!args || args.resource === undefined) && !opts.urn) {
                throw new Error("Missing required property 'resource'");
            }
            resourceInputs["lfTags"] = args ? args.lfTags : undefined;
            resourceInputs["resource"] = args ? args.resource : undefined;
            resourceInputs["resourceIdentifier"] = undefined /*out*/;
            resourceInputs["tagsIdentifier"] = undefined /*out*/;
        } else {
            resourceInputs["lfTags"] = undefined /*out*/;
            resourceInputs["resource"] = undefined /*out*/;
            resourceInputs["resourceIdentifier"] = undefined /*out*/;
            resourceInputs["tagsIdentifier"] = undefined /*out*/;
        }
        opts = pulumi.mergeOptions(utilities.resourceOptsDefaults(), opts);
        super(TagAssociation.__pulumiType, name, resourceInputs, opts);
    }
}

/**
 * The set of arguments for constructing a TagAssociation resource.
 */
export interface TagAssociationArgs {
    /**
     * List of Lake Formation Tags to associate with the Lake Formation Resource
     */
    lfTags: pulumi.Input<pulumi.Input<inputs.lakeformation.TagAssociationLFTagPairArgs>[]>;
    /**
     * Resource to tag with the Lake Formation Tags
     */
    resource: pulumi.Input<inputs.lakeformation.TagAssociationResourceArgs>;
}
