// *** WARNING: this file was generated by pulumigen. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

package workspaces

import (
	"context"
	"reflect"

	"github.com/pulumi/pulumi/sdk/v3/go/pulumi"
)

type ConnectionAliasConnectionAliasAssociation struct {
	AssociatedAccountId  *string                                                     `pulumi:"associatedAccountId"`
	AssociationStatus    *ConnectionAliasConnectionAliasAssociationAssociationStatus `pulumi:"associationStatus"`
	ConnectionIdentifier *string                                                     `pulumi:"connectionIdentifier"`
	ResourceId           *string                                                     `pulumi:"resourceId"`
}

// ConnectionAliasConnectionAliasAssociationInput is an input type that accepts ConnectionAliasConnectionAliasAssociationArgs and ConnectionAliasConnectionAliasAssociationOutput values.
// You can construct a concrete instance of `ConnectionAliasConnectionAliasAssociationInput` via:
//
//          ConnectionAliasConnectionAliasAssociationArgs{...}
type ConnectionAliasConnectionAliasAssociationInput interface {
	pulumi.Input

	ToConnectionAliasConnectionAliasAssociationOutput() ConnectionAliasConnectionAliasAssociationOutput
	ToConnectionAliasConnectionAliasAssociationOutputWithContext(context.Context) ConnectionAliasConnectionAliasAssociationOutput
}

type ConnectionAliasConnectionAliasAssociationArgs struct {
	AssociatedAccountId  pulumi.StringPtrInput                                              `pulumi:"associatedAccountId"`
	AssociationStatus    ConnectionAliasConnectionAliasAssociationAssociationStatusPtrInput `pulumi:"associationStatus"`
	ConnectionIdentifier pulumi.StringPtrInput                                              `pulumi:"connectionIdentifier"`
	ResourceId           pulumi.StringPtrInput                                              `pulumi:"resourceId"`
}

func (ConnectionAliasConnectionAliasAssociationArgs) ElementType() reflect.Type {
	return reflect.TypeOf((*ConnectionAliasConnectionAliasAssociation)(nil)).Elem()
}

func (i ConnectionAliasConnectionAliasAssociationArgs) ToConnectionAliasConnectionAliasAssociationOutput() ConnectionAliasConnectionAliasAssociationOutput {
	return i.ToConnectionAliasConnectionAliasAssociationOutputWithContext(context.Background())
}

func (i ConnectionAliasConnectionAliasAssociationArgs) ToConnectionAliasConnectionAliasAssociationOutputWithContext(ctx context.Context) ConnectionAliasConnectionAliasAssociationOutput {
	return pulumi.ToOutputWithContext(ctx, i).(ConnectionAliasConnectionAliasAssociationOutput)
}

// ConnectionAliasConnectionAliasAssociationArrayInput is an input type that accepts ConnectionAliasConnectionAliasAssociationArray and ConnectionAliasConnectionAliasAssociationArrayOutput values.
// You can construct a concrete instance of `ConnectionAliasConnectionAliasAssociationArrayInput` via:
//
//          ConnectionAliasConnectionAliasAssociationArray{ ConnectionAliasConnectionAliasAssociationArgs{...} }
type ConnectionAliasConnectionAliasAssociationArrayInput interface {
	pulumi.Input

	ToConnectionAliasConnectionAliasAssociationArrayOutput() ConnectionAliasConnectionAliasAssociationArrayOutput
	ToConnectionAliasConnectionAliasAssociationArrayOutputWithContext(context.Context) ConnectionAliasConnectionAliasAssociationArrayOutput
}

type ConnectionAliasConnectionAliasAssociationArray []ConnectionAliasConnectionAliasAssociationInput

func (ConnectionAliasConnectionAliasAssociationArray) ElementType() reflect.Type {
	return reflect.TypeOf((*[]ConnectionAliasConnectionAliasAssociation)(nil)).Elem()
}

func (i ConnectionAliasConnectionAliasAssociationArray) ToConnectionAliasConnectionAliasAssociationArrayOutput() ConnectionAliasConnectionAliasAssociationArrayOutput {
	return i.ToConnectionAliasConnectionAliasAssociationArrayOutputWithContext(context.Background())
}

func (i ConnectionAliasConnectionAliasAssociationArray) ToConnectionAliasConnectionAliasAssociationArrayOutputWithContext(ctx context.Context) ConnectionAliasConnectionAliasAssociationArrayOutput {
	return pulumi.ToOutputWithContext(ctx, i).(ConnectionAliasConnectionAliasAssociationArrayOutput)
}

type ConnectionAliasConnectionAliasAssociationOutput struct{ *pulumi.OutputState }

func (ConnectionAliasConnectionAliasAssociationOutput) ElementType() reflect.Type {
	return reflect.TypeOf((*ConnectionAliasConnectionAliasAssociation)(nil)).Elem()
}

func (o ConnectionAliasConnectionAliasAssociationOutput) ToConnectionAliasConnectionAliasAssociationOutput() ConnectionAliasConnectionAliasAssociationOutput {
	return o
}

func (o ConnectionAliasConnectionAliasAssociationOutput) ToConnectionAliasConnectionAliasAssociationOutputWithContext(ctx context.Context) ConnectionAliasConnectionAliasAssociationOutput {
	return o
}

func (o ConnectionAliasConnectionAliasAssociationOutput) AssociatedAccountId() pulumi.StringPtrOutput {
	return o.ApplyT(func(v ConnectionAliasConnectionAliasAssociation) *string { return v.AssociatedAccountId }).(pulumi.StringPtrOutput)
}

func (o ConnectionAliasConnectionAliasAssociationOutput) AssociationStatus() ConnectionAliasConnectionAliasAssociationAssociationStatusPtrOutput {
	return o.ApplyT(func(v ConnectionAliasConnectionAliasAssociation) *ConnectionAliasConnectionAliasAssociationAssociationStatus {
		return v.AssociationStatus
	}).(ConnectionAliasConnectionAliasAssociationAssociationStatusPtrOutput)
}

func (o ConnectionAliasConnectionAliasAssociationOutput) ConnectionIdentifier() pulumi.StringPtrOutput {
	return o.ApplyT(func(v ConnectionAliasConnectionAliasAssociation) *string { return v.ConnectionIdentifier }).(pulumi.StringPtrOutput)
}

func (o ConnectionAliasConnectionAliasAssociationOutput) ResourceId() pulumi.StringPtrOutput {
	return o.ApplyT(func(v ConnectionAliasConnectionAliasAssociation) *string { return v.ResourceId }).(pulumi.StringPtrOutput)
}

type ConnectionAliasConnectionAliasAssociationArrayOutput struct{ *pulumi.OutputState }

func (ConnectionAliasConnectionAliasAssociationArrayOutput) ElementType() reflect.Type {
	return reflect.TypeOf((*[]ConnectionAliasConnectionAliasAssociation)(nil)).Elem()
}

func (o ConnectionAliasConnectionAliasAssociationArrayOutput) ToConnectionAliasConnectionAliasAssociationArrayOutput() ConnectionAliasConnectionAliasAssociationArrayOutput {
	return o
}

func (o ConnectionAliasConnectionAliasAssociationArrayOutput) ToConnectionAliasConnectionAliasAssociationArrayOutputWithContext(ctx context.Context) ConnectionAliasConnectionAliasAssociationArrayOutput {
	return o
}

func (o ConnectionAliasConnectionAliasAssociationArrayOutput) Index(i pulumi.IntInput) ConnectionAliasConnectionAliasAssociationOutput {
	return pulumi.All(o, i).ApplyT(func(vs []interface{}) ConnectionAliasConnectionAliasAssociation {
		return vs[0].([]ConnectionAliasConnectionAliasAssociation)[vs[1].(int)]
	}).(ConnectionAliasConnectionAliasAssociationOutput)
}

type ConnectionAliasTag struct {
	Key   string `pulumi:"key"`
	Value string `pulumi:"value"`
}

// ConnectionAliasTagInput is an input type that accepts ConnectionAliasTagArgs and ConnectionAliasTagOutput values.
// You can construct a concrete instance of `ConnectionAliasTagInput` via:
//
//          ConnectionAliasTagArgs{...}
type ConnectionAliasTagInput interface {
	pulumi.Input

	ToConnectionAliasTagOutput() ConnectionAliasTagOutput
	ToConnectionAliasTagOutputWithContext(context.Context) ConnectionAliasTagOutput
}

type ConnectionAliasTagArgs struct {
	Key   pulumi.StringInput `pulumi:"key"`
	Value pulumi.StringInput `pulumi:"value"`
}

func (ConnectionAliasTagArgs) ElementType() reflect.Type {
	return reflect.TypeOf((*ConnectionAliasTag)(nil)).Elem()
}

func (i ConnectionAliasTagArgs) ToConnectionAliasTagOutput() ConnectionAliasTagOutput {
	return i.ToConnectionAliasTagOutputWithContext(context.Background())
}

func (i ConnectionAliasTagArgs) ToConnectionAliasTagOutputWithContext(ctx context.Context) ConnectionAliasTagOutput {
	return pulumi.ToOutputWithContext(ctx, i).(ConnectionAliasTagOutput)
}

// ConnectionAliasTagArrayInput is an input type that accepts ConnectionAliasTagArray and ConnectionAliasTagArrayOutput values.
// You can construct a concrete instance of `ConnectionAliasTagArrayInput` via:
//
//          ConnectionAliasTagArray{ ConnectionAliasTagArgs{...} }
type ConnectionAliasTagArrayInput interface {
	pulumi.Input

	ToConnectionAliasTagArrayOutput() ConnectionAliasTagArrayOutput
	ToConnectionAliasTagArrayOutputWithContext(context.Context) ConnectionAliasTagArrayOutput
}

type ConnectionAliasTagArray []ConnectionAliasTagInput

func (ConnectionAliasTagArray) ElementType() reflect.Type {
	return reflect.TypeOf((*[]ConnectionAliasTag)(nil)).Elem()
}

func (i ConnectionAliasTagArray) ToConnectionAliasTagArrayOutput() ConnectionAliasTagArrayOutput {
	return i.ToConnectionAliasTagArrayOutputWithContext(context.Background())
}

func (i ConnectionAliasTagArray) ToConnectionAliasTagArrayOutputWithContext(ctx context.Context) ConnectionAliasTagArrayOutput {
	return pulumi.ToOutputWithContext(ctx, i).(ConnectionAliasTagArrayOutput)
}

type ConnectionAliasTagOutput struct{ *pulumi.OutputState }

func (ConnectionAliasTagOutput) ElementType() reflect.Type {
	return reflect.TypeOf((*ConnectionAliasTag)(nil)).Elem()
}

func (o ConnectionAliasTagOutput) ToConnectionAliasTagOutput() ConnectionAliasTagOutput {
	return o
}

func (o ConnectionAliasTagOutput) ToConnectionAliasTagOutputWithContext(ctx context.Context) ConnectionAliasTagOutput {
	return o
}

func (o ConnectionAliasTagOutput) Key() pulumi.StringOutput {
	return o.ApplyT(func(v ConnectionAliasTag) string { return v.Key }).(pulumi.StringOutput)
}

func (o ConnectionAliasTagOutput) Value() pulumi.StringOutput {
	return o.ApplyT(func(v ConnectionAliasTag) string { return v.Value }).(pulumi.StringOutput)
}

type ConnectionAliasTagArrayOutput struct{ *pulumi.OutputState }

func (ConnectionAliasTagArrayOutput) ElementType() reflect.Type {
	return reflect.TypeOf((*[]ConnectionAliasTag)(nil)).Elem()
}

func (o ConnectionAliasTagArrayOutput) ToConnectionAliasTagArrayOutput() ConnectionAliasTagArrayOutput {
	return o
}

func (o ConnectionAliasTagArrayOutput) ToConnectionAliasTagArrayOutputWithContext(ctx context.Context) ConnectionAliasTagArrayOutput {
	return o
}

func (o ConnectionAliasTagArrayOutput) Index(i pulumi.IntInput) ConnectionAliasTagOutput {
	return pulumi.All(o, i).ApplyT(func(vs []interface{}) ConnectionAliasTag {
		return vs[0].([]ConnectionAliasTag)[vs[1].(int)]
	}).(ConnectionAliasTagOutput)
}

func init() {
	pulumi.RegisterOutputType(ConnectionAliasConnectionAliasAssociationOutput{})
	pulumi.RegisterOutputType(ConnectionAliasConnectionAliasAssociationArrayOutput{})
	pulumi.RegisterOutputType(ConnectionAliasTagOutput{})
	pulumi.RegisterOutputType(ConnectionAliasTagArrayOutput{})
}
