// *** WARNING: this file was generated by the Pulumi SDK Generator. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

import * as pulumi from "@pulumi/pulumi";
import * as inputs from "../types/input";
import * as outputs from "../types/output";
import * as enums from "../types/enums";
import * as utilities from "../utilities";

/**
 * A Bot Alias enables you to change the version of a bot without updating applications that use the bot
 */
export class BotAlias extends pulumi.CustomResource {
    /**
     * Get an existing BotAlias resource's state with the given name, ID, and optional extra
     * properties used to qualify the lookup.
     *
     * @param name The _unique_ name of the resulting resource.
     * @param id The _unique_ provider ID of the resource to lookup.
     * @param opts Optional settings to control the behavior of the CustomResource.
     */
    public static get(name: string, id: pulumi.Input<pulumi.ID>, opts?: pulumi.CustomResourceOptions): BotAlias {
        return new BotAlias(name, undefined as any, { ...opts, id: id });
    }

    /** @internal */
    public static readonly __pulumiType = 'aws-native:lex:BotAlias';

    /**
     * Returns true if the given object is an instance of BotAlias.  This is designed to work even
     * when multiple copies of the Pulumi SDK have been loaded into the same process.
     */
    public static isInstance(obj: any): obj is BotAlias {
        if (obj === undefined || obj === null) {
            return false;
        }
        return obj['__pulumiType'] === BotAlias.__pulumiType;
    }

    public /*out*/ readonly arn!: pulumi.Output<string>;
    public /*out*/ readonly botAliasId!: pulumi.Output<string>;
    public readonly botAliasLocaleSettings!: pulumi.Output<outputs.lex.BotAliasLocaleSettingsItem[] | undefined>;
    public readonly botAliasName!: pulumi.Output<string>;
    public /*out*/ readonly botAliasStatus!: pulumi.Output<enums.lex.BotAliasStatus>;
    /**
     * A list of tags to add to the bot alias.
     */
    public readonly botAliasTags!: pulumi.Output<outputs.lex.BotAliasTag[] | undefined>;
    public readonly botId!: pulumi.Output<string>;
    public readonly botVersion!: pulumi.Output<string | undefined>;
    public readonly conversationLogSettings!: pulumi.Output<outputs.lex.BotAliasConversationLogSettings | undefined>;
    public readonly description!: pulumi.Output<string | undefined>;
    /**
     * Determines whether Amazon Lex will use Amazon Comprehend to detect the sentiment of user utterances.
     */
    public readonly sentimentAnalysisSettings!: pulumi.Output<outputs.lex.SentimentAnalysisSettingsProperties | undefined>;

    /**
     * Create a BotAlias resource with the given unique name, arguments, and options.
     *
     * @param name The _unique_ name of the resource.
     * @param args The arguments to use to populate this resource's properties.
     * @param opts A bag of options that control this resource's behavior.
     */
    constructor(name: string, args: BotAliasArgs, opts?: pulumi.CustomResourceOptions) {
        let resourceInputs: pulumi.Inputs = {};
        opts = opts || {};
        if (!opts.id) {
            if ((!args || args.botId === undefined) && !opts.urn) {
                throw new Error("Missing required property 'botId'");
            }
            resourceInputs["botAliasLocaleSettings"] = args ? args.botAliasLocaleSettings : undefined;
            resourceInputs["botAliasName"] = args ? args.botAliasName : undefined;
            resourceInputs["botAliasTags"] = args ? args.botAliasTags : undefined;
            resourceInputs["botId"] = args ? args.botId : undefined;
            resourceInputs["botVersion"] = args ? args.botVersion : undefined;
            resourceInputs["conversationLogSettings"] = args ? args.conversationLogSettings : undefined;
            resourceInputs["description"] = args ? args.description : undefined;
            resourceInputs["sentimentAnalysisSettings"] = args ? args.sentimentAnalysisSettings : undefined;
            resourceInputs["arn"] = undefined /*out*/;
            resourceInputs["botAliasId"] = undefined /*out*/;
            resourceInputs["botAliasStatus"] = undefined /*out*/;
        } else {
            resourceInputs["arn"] = undefined /*out*/;
            resourceInputs["botAliasId"] = undefined /*out*/;
            resourceInputs["botAliasLocaleSettings"] = undefined /*out*/;
            resourceInputs["botAliasName"] = undefined /*out*/;
            resourceInputs["botAliasStatus"] = undefined /*out*/;
            resourceInputs["botAliasTags"] = undefined /*out*/;
            resourceInputs["botId"] = undefined /*out*/;
            resourceInputs["botVersion"] = undefined /*out*/;
            resourceInputs["conversationLogSettings"] = undefined /*out*/;
            resourceInputs["description"] = undefined /*out*/;
            resourceInputs["sentimentAnalysisSettings"] = undefined /*out*/;
        }
        opts = pulumi.mergeOptions(utilities.resourceOptsDefaults(), opts);
        super(BotAlias.__pulumiType, name, resourceInputs, opts);
    }
}

/**
 * The set of arguments for constructing a BotAlias resource.
 */
export interface BotAliasArgs {
    botAliasLocaleSettings?: pulumi.Input<pulumi.Input<inputs.lex.BotAliasLocaleSettingsItemArgs>[]>;
    botAliasName?: pulumi.Input<string>;
    /**
     * A list of tags to add to the bot alias.
     */
    botAliasTags?: pulumi.Input<pulumi.Input<inputs.lex.BotAliasTagArgs>[]>;
    botId: pulumi.Input<string>;
    botVersion?: pulumi.Input<string>;
    conversationLogSettings?: pulumi.Input<inputs.lex.BotAliasConversationLogSettingsArgs>;
    description?: pulumi.Input<string>;
    /**
     * Determines whether Amazon Lex will use Amazon Comprehend to detect the sentiment of user utterances.
     */
    sentimentAnalysisSettings?: pulumi.Input<inputs.lex.SentimentAnalysisSettingsPropertiesArgs>;
}
