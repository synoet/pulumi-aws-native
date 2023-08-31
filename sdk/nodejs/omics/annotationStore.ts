// *** WARNING: this file was generated by the Pulumi SDK Generator. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

import * as pulumi from "@pulumi/pulumi";
import * as inputs from "../types/input";
import * as outputs from "../types/output";
import * as enums from "../types/enums";
import * as utilities from "../utilities";

/**
 * Definition of AWS::Omics::AnnotationStore Resource Type
 */
export class AnnotationStore extends pulumi.CustomResource {
    /**
     * Get an existing AnnotationStore resource's state with the given name, ID, and optional extra
     * properties used to qualify the lookup.
     *
     * @param name The _unique_ name of the resulting resource.
     * @param id The _unique_ provider ID of the resource to lookup.
     * @param opts Optional settings to control the behavior of the CustomResource.
     */
    public static get(name: string, id: pulumi.Input<pulumi.ID>, opts?: pulumi.CustomResourceOptions): AnnotationStore {
        return new AnnotationStore(name, undefined as any, { ...opts, id: id });
    }

    /** @internal */
    public static readonly __pulumiType = 'aws-native:omics:AnnotationStore';

    /**
     * Returns true if the given object is an instance of AnnotationStore.  This is designed to work even
     * when multiple copies of the Pulumi SDK have been loaded into the same process.
     */
    public static isInstance(obj: any): obj is AnnotationStore {
        if (obj === undefined || obj === null) {
            return false;
        }
        return obj['__pulumiType'] === AnnotationStore.__pulumiType;
    }

    public /*out*/ readonly creationTime!: pulumi.Output<string>;
    public readonly description!: pulumi.Output<string | undefined>;
    public readonly name!: pulumi.Output<string>;
    public readonly reference!: pulumi.Output<outputs.omics.AnnotationStoreReferenceItem | undefined>;
    public readonly sseConfig!: pulumi.Output<outputs.omics.AnnotationStoreSseConfig | undefined>;
    public /*out*/ readonly status!: pulumi.Output<enums.omics.AnnotationStoreStoreStatus>;
    public /*out*/ readonly statusMessage!: pulumi.Output<string>;
    public /*out*/ readonly storeArn!: pulumi.Output<string>;
    public readonly storeFormat!: pulumi.Output<enums.omics.AnnotationStoreStoreFormat>;
    public readonly storeOptions!: pulumi.Output<outputs.omics.AnnotationStoreStoreOptionsProperties | undefined>;
    public /*out*/ readonly storeSizeBytes!: pulumi.Output<number>;
    public readonly tags!: pulumi.Output<outputs.omics.AnnotationStoreTagMap | undefined>;
    public /*out*/ readonly updateTime!: pulumi.Output<string>;

    /**
     * Create a AnnotationStore resource with the given unique name, arguments, and options.
     *
     * @param name The _unique_ name of the resource.
     * @param args The arguments to use to populate this resource's properties.
     * @param opts A bag of options that control this resource's behavior.
     */
    constructor(name: string, args: AnnotationStoreArgs, opts?: pulumi.CustomResourceOptions) {
        let resourceInputs: pulumi.Inputs = {};
        opts = opts || {};
        if (!opts.id) {
            if ((!args || args.storeFormat === undefined) && !opts.urn) {
                throw new Error("Missing required property 'storeFormat'");
            }
            resourceInputs["description"] = args ? args.description : undefined;
            resourceInputs["name"] = args ? args.name : undefined;
            resourceInputs["reference"] = args ? args.reference : undefined;
            resourceInputs["sseConfig"] = args ? args.sseConfig : undefined;
            resourceInputs["storeFormat"] = args ? args.storeFormat : undefined;
            resourceInputs["storeOptions"] = args ? args.storeOptions : undefined;
            resourceInputs["tags"] = args ? args.tags : undefined;
            resourceInputs["creationTime"] = undefined /*out*/;
            resourceInputs["status"] = undefined /*out*/;
            resourceInputs["statusMessage"] = undefined /*out*/;
            resourceInputs["storeArn"] = undefined /*out*/;
            resourceInputs["storeSizeBytes"] = undefined /*out*/;
            resourceInputs["updateTime"] = undefined /*out*/;
        } else {
            resourceInputs["creationTime"] = undefined /*out*/;
            resourceInputs["description"] = undefined /*out*/;
            resourceInputs["name"] = undefined /*out*/;
            resourceInputs["reference"] = undefined /*out*/;
            resourceInputs["sseConfig"] = undefined /*out*/;
            resourceInputs["status"] = undefined /*out*/;
            resourceInputs["statusMessage"] = undefined /*out*/;
            resourceInputs["storeArn"] = undefined /*out*/;
            resourceInputs["storeFormat"] = undefined /*out*/;
            resourceInputs["storeOptions"] = undefined /*out*/;
            resourceInputs["storeSizeBytes"] = undefined /*out*/;
            resourceInputs["tags"] = undefined /*out*/;
            resourceInputs["updateTime"] = undefined /*out*/;
        }
        opts = pulumi.mergeOptions(utilities.resourceOptsDefaults(), opts);
        const replaceOnChanges = { replaceOnChanges: ["name", "reference", "sseConfig", "storeFormat", "storeOptions", "tags"] };
        opts = pulumi.mergeOptions(opts, replaceOnChanges);
        super(AnnotationStore.__pulumiType, name, resourceInputs, opts);
    }
}

/**
 * The set of arguments for constructing a AnnotationStore resource.
 */
export interface AnnotationStoreArgs {
    description?: pulumi.Input<string>;
    name?: pulumi.Input<string>;
    reference?: pulumi.Input<inputs.omics.AnnotationStoreReferenceItemArgs>;
    sseConfig?: pulumi.Input<inputs.omics.AnnotationStoreSseConfigArgs>;
    storeFormat: pulumi.Input<enums.omics.AnnotationStoreStoreFormat>;
    storeOptions?: pulumi.Input<inputs.omics.AnnotationStoreStoreOptionsPropertiesArgs>;
    tags?: pulumi.Input<inputs.omics.AnnotationStoreTagMapArgs>;
}
