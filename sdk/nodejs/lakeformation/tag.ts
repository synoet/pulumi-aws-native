// *** WARNING: this file was generated by the Pulumi SDK Generator. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

import * as pulumi from "@pulumi/pulumi";
import * as utilities from "../utilities";

/**
 * A resource schema representing a Lake Formation Tag.
 */
export class Tag extends pulumi.CustomResource {
    /**
     * Get an existing Tag resource's state with the given name, ID, and optional extra
     * properties used to qualify the lookup.
     *
     * @param name The _unique_ name of the resulting resource.
     * @param id The _unique_ provider ID of the resource to lookup.
     * @param opts Optional settings to control the behavior of the CustomResource.
     */
    public static get(name: string, id: pulumi.Input<pulumi.ID>, opts?: pulumi.CustomResourceOptions): Tag {
        return new Tag(name, undefined as any, { ...opts, id: id });
    }

    /** @internal */
    public static readonly __pulumiType = 'aws-native:lakeformation:Tag';

    /**
     * Returns true if the given object is an instance of Tag.  This is designed to work even
     * when multiple copies of the Pulumi SDK have been loaded into the same process.
     */
    public static isInstance(obj: any): obj is Tag {
        if (obj === undefined || obj === null) {
            return false;
        }
        return obj['__pulumiType'] === Tag.__pulumiType;
    }

    /**
     * The identifier for the Data Catalog. By default, the account ID. The Data Catalog is the persistent metadata store. It contains database definitions, table definitions, and other control information to manage your Lake Formation environment.
     */
    public readonly catalogId!: pulumi.Output<string | undefined>;
    /**
     * The key-name for the LF-tag.
     */
    public readonly tagKey!: pulumi.Output<string>;
    /**
     * A list of possible values an attribute can take.
     */
    public readonly tagValues!: pulumi.Output<string[]>;

    /**
     * Create a Tag resource with the given unique name, arguments, and options.
     *
     * @param name The _unique_ name of the resource.
     * @param args The arguments to use to populate this resource's properties.
     * @param opts A bag of options that control this resource's behavior.
     */
    constructor(name: string, args: TagArgs, opts?: pulumi.CustomResourceOptions) {
        let resourceInputs: pulumi.Inputs = {};
        opts = opts || {};
        if (!opts.id) {
            if ((!args || args.tagKey === undefined) && !opts.urn) {
                throw new Error("Missing required property 'tagKey'");
            }
            if ((!args || args.tagValues === undefined) && !opts.urn) {
                throw new Error("Missing required property 'tagValues'");
            }
            resourceInputs["catalogId"] = args ? args.catalogId : undefined;
            resourceInputs["tagKey"] = args ? args.tagKey : undefined;
            resourceInputs["tagValues"] = args ? args.tagValues : undefined;
        } else {
            resourceInputs["catalogId"] = undefined /*out*/;
            resourceInputs["tagKey"] = undefined /*out*/;
            resourceInputs["tagValues"] = undefined /*out*/;
        }
        opts = pulumi.mergeOptions(utilities.resourceOptsDefaults(), opts);
        const replaceOnChanges = { replaceOnChanges: ["catalogId", "tagKey"] };
        opts = pulumi.mergeOptions(opts, replaceOnChanges);
        super(Tag.__pulumiType, name, resourceInputs, opts);
    }
}

/**
 * The set of arguments for constructing a Tag resource.
 */
export interface TagArgs {
    /**
     * The identifier for the Data Catalog. By default, the account ID. The Data Catalog is the persistent metadata store. It contains database definitions, table definitions, and other control information to manage your Lake Formation environment.
     */
    catalogId?: pulumi.Input<string>;
    /**
     * The key-name for the LF-tag.
     */
    tagKey: pulumi.Input<string>;
    /**
     * A list of possible values an attribute can take.
     */
    tagValues: pulumi.Input<pulumi.Input<string>[]>;
}
